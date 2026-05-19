from machine import Pin, ADC, PWM, I2C, reset
import ssd1306
import network
import socket
import time

# WiFi
SSID = "FRITZ!Box 6670 TT"
PASSWORD = "61780260652741072738"

# RGB LED - Common Anode
red = PWM(Pin(14))
green = PWM(Pin(26))
blue = PWM(Pin(13))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Sensors
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

motion_sensor = Pin(27, Pin.IN)

# OLED
i2c = I2C(0, scl=Pin(33), sda=Pin(32), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# System States
system_mode = "AUTO"

motion_timeout = 5
last_motion_time = 0

current_color = (0, 0, 0)

light_value = 0
motion_text = "NO"
light_state = "BRIGHT"
rgb_status = "OFF"

# RGB Functions
def set_color(r, g, b):
    red.duty(1023 - r)
    green.duty(1023 - g)
    blue.duty(1023 - b)

def fade_color(start, end, steps=15, delay=0.005):
    for i in range(steps + 1):
        r = int(start[0] + (end[0] - start[0]) * i / steps)
        g = int(start[1] + (end[1] - start[1]) * i / steps)
        b = int(start[2] + (end[2] - start[2]) * i / steps)
        set_color(r, g, b)
        time.sleep(delay)

def go_to_color(target):
    global current_color
    if current_color != target:
        fade_color(current_color, target)
        current_color = target

# OLED
def update_oled():
    oled.fill(0)
    oled.text("Smart Room V3", 0, 0)
    oled.text("Mode:", 0, 12)
    oled.text(system_mode, 45, 12)
    oled.text("Light:", 0, 24)
    oled.text(str(light_value), 50, 24)
    oled.text("State:", 0, 36)
    oled.text(light_state, 50, 36)
    oled.text("Motion:", 0, 48)
    oled.text(motion_text, 60, 48)
    oled.text("RGB: " + rgb_status, 0, 56)
    oled.show()

# WiFi Connect
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting to WiFi...")

while not wifi.isconnected():
    print("Connecting...")
    time.sleep(1)

ip = wifi.ifconfig()[0]

print("Connected!")
print("IP:", ip)

# Web Page
def webpage():
    html = f"""
<html>
<head>
<title>ESP32 Smart Room Controller V3</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="5">

<style>
body {{
    background: #111827;
    color: white;
    font-family: Arial;
    text-align: center;
    padding-top: 35px;
}}

.box {{
    background: #1f2937;
    width: 85%;
    max-width: 650px;
    margin: auto;
    padding: 30px;
    border-radius: 20px;
}}

h1 {{
    font-size: 40px;
    color: #38bdf8;
}}

h2 {{
    font-size: 26px;
}}

button {{
    width: 260px;
    height: 60px;
    border: none;
    border-radius: 15px;
    margin: 10px;
    font-size: 22px;
    font-weight: bold;
}}

.auto {{
    background: #38bdf8;
}}

.on {{
    background: #22c55e;
}}

.off {{
    background: #ef4444;
    color: white;
}}

.restart {{
    background: #f59e0b;
}}

.footer {{
    position: fixed;
    left: 20px;
    bottom: 10px;
    font-size: 22px;
    color: #cbd5e1;
    text-align: left;
}}
</style>
</head>

<body>
<div class="box">
<h1>ESP32 Smart Room Controller V3</h1>

<h2>Mode: {system_mode}</h2>
<h2>Light: {light_value}</h2>
<h2>State: {light_state}</h2>
<h2>Motion: {motion_text}</h2>
<h2>RGB: {rgb_status}</h2>

<a href="/auto"><button class="auto">AUTO MODE</button></a><br>
<a href="/on"><button class="on">MANUAL ON</button></a><br>
<a href="/off"><button class="off">MANUAL OFF</button></a><br>
<a href="/restart"><button class="restart">RESTART ESP32</button></a>
</div>

<div class="footer">
Ahmad Azroun<br>
Renewable Energy Manager<br>
IoT & Smart Energy Systems Developer
</div>

</body>
</html>
"""
    return html

# Web Server
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(5)
server.settimeout(0.05)

print("Web Server Running...")
print("Open: http://" + ip)

update_oled()

# Main Loop
while True:

    # Web Request - Non Blocking
    try:
        client, addr = server.accept()
        request = client.recv(1024).decode()

        first_line = request.split("\r\n")[0]
        print("Request:", first_line)

        if "GET /auto " in first_line:
            system_mode = "AUTO"
            print("Web Mode: AUTO")

        elif "GET /on " in first_line:
            system_mode = "MANUAL_ON"
            print("Web Mode: MANUAL ON")

        elif "GET /off " in first_line:
            system_mode = "MANUAL_OFF"
            print("Web Mode: MANUAL OFF")

        elif "GET /restart " in first_line:
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            client.send("<h1>Restarting ESP32...</h1>")
            client.close()
            time.sleep(1)
            reset()

        response = webpage()

        client.send("HTTP/1.1 200 OK\r\n")
        client.send("Content-Type: text/html\r\n")
        client.send("Connection: close\r\n\r\n")
        client.sendall(response)
        client.close()

    except OSError:
        pass

    # Read Sensors Always
    light_value = light_sensor.read()
    motion = motion_sensor.value()
    motion_text = "YES" if motion == 1 else "NO"

    # AUTO MODE
    if system_mode == "AUTO":

        if light_value < 1800:
            light_state = "BRIGHT"
            rgb_status = "OFF"
            go_to_color((0, 0, 0))

        else:
            light_state = "DARK"

            if motion == 1:
                last_motion_time = time.time()
                rgb_status = "WHITE"
                go_to_color((500, 500, 500))

            else:
                elapsed = time.time() - last_motion_time

                if elapsed < motion_timeout:
                    rgb_status = "WHITE"
                    go_to_color((500, 500, 500))
                else:
                    rgb_status = "DIM BLUE"
                    go_to_color((0, 0, 120))

    # MANUAL ON
    elif system_mode == "MANUAL_ON":
        light_state = "-"
        motion_text = "-"
        rgb_status = "GREEN"
        go_to_color((0, 500, 0))

    # MANUAL OFF
    elif system_mode == "MANUAL_OFF":
        light_state = "-"
        motion_text = "-"
        rgb_status = "RED"
        go_to_color((500, 0, 0))

    update_oled()

    print("Mode:", system_mode)
    print("Light:", light_value)
    print("State:", light_state)
    print("Motion:", motion_text)
    print("RGB:", rgb_status)
    print("----------------------")

    time.sleep(0.1)
