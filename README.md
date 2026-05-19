# ESP32 Smart Room Controller V3

---

#  Deutsche Version

## Projektbeschreibung

Dieses Projekt demonstriert ein professionelles Smart-Room-Controller-System mit einem ESP32 Mikrocontroller, OLED Display, PIR-Bewegungssensor, LDR-Lichtsensor, RGB-LED und einem modernen WiFi-Webdashboard.

Das System erkennt automatisch die Umgebungshelligkeit sowie Bewegungen im Raum und steuert die RGB-Beleuchtung intelligent und energieeffizient.

Zusätzlich ermöglicht das integrierte WiFi-Webinterface eine vollständige Fernsteuerung des Systems über Smartphone, Tablet oder Computer.

Das Projekt kombiniert moderne IoT-Technologien, Smart-Home-Automatisierung, Sensorintegration und Embedded-System-Programmierung mit MicroPython.

---

# Hauptfunktionen

- WiFi Web Dashboard
- Live-Systemüberwachung
- OLED Echtzeit-Anzeige
- Automatische Lichtsteuerung
- Bewegungserkennung mit PIR-Sensor
- RGB LED Steuerung mit PWM
- AUTO MODE
- MANUAL ON MODE
- MANUAL OFF MODE
- ESP32 Neustart über Webinterface
- Energieeffiziente Beleuchtungslogik
- Sanfte RGB-Farbwechsel
- Smart Home Integration
- IoT-basierte Fernsteuerung

---

# Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | Hauptcontroller des Systems |
| OLED Display SSD1306 | Echtzeit-Systemanzeige |
| PIR Motion Sensor | Bewegungserkennung |
| LDR Sensor | Umgebungshelligkeit messen |
| RGB LED (Common Anode) | Status- und Lichtanzeige |
| Push Button | Manuelle Steuerung |
| Breadboard | Schaltungsaufbau |
| Jumper Kabel | Elektrische Verbindungen |
| Widerstände | Schutz der RGB-LED |

---

# Pin-Verbindungen

| Komponente | ESP32 Pin |
|---|---|
| RGB Rot | GPIO14 |
| RGB Grün | GPIO26 |
| RGB Blau | GPIO13 |
| PIR Sensor OUT | GPIO27 |
| LDR Sensor AO | GPIO34 |
| OLED SDA | GPIO32 |
| OLED SCL | GPIO33 |
| Push Button | GPIO25 |

---

# RGB Farbmodi

| Modus | Farbe | Beschreibung |
|---|---|---|
| Helle Umgebung | AUS | Es ist genug Licht vorhanden |
| Dunkle Umgebung ohne Bewegung | Blau | Energiesparender Nachtmodus |
| Dunkle Umgebung mit Bewegung | Weiß | Bewegung erkannt |
| MANUAL ON MODE | Grün | Benutzer aktiviert System |
| MANUAL OFF MODE | Rot | Benutzer deaktiviert System |

---

# Betriebsmodi

## AUTO MODE

Das System arbeitet vollständig automatisch:

- Der LDR misst die Helligkeit.
- Der PIR-Sensor erkennt Bewegungen.
- Das RGB-Licht reagiert automatisch abhängig von Licht und Bewegung.

---

## MANUAL ON MODE

- Das RGB-Licht wird manuell aktiviert.
- Die RGB-LED leuchtet dauerhaft grün.
- Das System ignoriert Sensorwerte.

---

## MANUAL OFF MODE

- Das System wird manuell deaktiviert.
- Die RGB-LED leuchtet rot.
- Automatische Funktionen werden deaktiviert.

---

# OLED Display Funktionen

Das OLED Display zeigt in Echtzeit:

- Aktuellen Betriebsmodus
- Lichtwert
- Bewegungsstatus
- RGB Status
- Systeminformationen

Dadurch kann der Benutzer das gesamte System lokal überwachen.

---

# WiFi Web Dashboard

Das Projekt besitzt ein modernes WiFi-Webdashboard.

Funktionen des Dashboards:

- Anzeige aller Live-Daten
- Steuerung aller Betriebsmodi
- Fernzugriff über Smartphone
- Neustart des ESP32
- Benutzerfreundliche Oberfläche
- Echtzeit-Aktualisierung

---

# Systemlogik

1. Das System verbindet sich mit dem WLAN.
2. Der ESP32 startet den lokalen Webserver.
3. Sensorwerte werden permanent überwacht.
4. Das OLED Display aktualisiert Live-Daten.
5. Das RGB-Licht reagiert abhängig von Bewegung und Helligkeit.
6. Benutzer können das System über das Dashboard steuern.
7. Alle Zustände werden in Echtzeit synchronisiert.

---

# Praktische Anwendungen

Dieses Projekt kann in vielen realen Anwendungen eingesetzt werden:

- Smart-Home-Beleuchtungssysteme
- Energieeffiziente Raumsteuerung
- Automatische Nachtbeleuchtung
- IoT-basierte Gebäudeautomatisierung
- Intelligente Smart-Building-Systeme
- Embedded- und IoT-Lernplattformen
- Prototypen für Smart-Energy-Systeme
- Sicherheitsbeleuchtung
- Intelligente Flurbeleuchtung
- Garagenautomatisierung
- Bewegungsgesteuerte Beleuchtung
- Smart-City Anwendungen
- Industrie-Überwachungssysteme

---

# Verwendete Technologien

- ESP32 Microcontroller
- MicroPython
- Embedded Systems
- WiFi Networking
- IoT Systems
- PWM RGB Control
- Sensor Integration
- OLED Display Communication
- Web Server Programming
- Smart Home Automation

---

# Benötigte Bibliotheken

```python
import network
import socket
import machine
import time
import ssd1306
```

Zusätzlich muss die Datei `ssd1306.py` auf den ESP32 hochgeladen werden.

---

# Vollständiger MicroPython Code

```python
# Full ESP32 Smart Room Controller V3 Source Code
# OLED + WiFi Dashboard + RGB + PIR + LDR + Web Control
```

---

# Entwickler

## Ahmad Azroun

Renewable Energy Manager | IoT & Smart Energy Systems Developer

---

#  English Version

## Project Description

This project demonstrates a professional Smart Room Controller system using an ESP32 microcontroller, OLED display, PIR motion sensor, LDR light sensor, RGB LED, and a modern WiFi web dashboard.

The system automatically detects ambient brightness and motion inside the room and intelligently controls the RGB lighting system in an energy-efficient way.

Additionally, the integrated WiFi dashboard allows complete remote system control through smartphones, tablets, or computers.

The project combines modern IoT technologies, smart home automation, sensor integration, and embedded systems programming using MicroPython.

---

# Main Features

- WiFi Web Dashboard
- Live System Monitoring
- OLED Real-Time Display
- Automatic Lighting Control
- Motion Detection using PIR Sensor
- RGB LED PWM Control
- AUTO MODE
- MANUAL ON MODE
- MANUAL OFF MODE
- ESP32 Restart via Web Interface
- Energy-Efficient Lighting Logic
- Smooth RGB Color Transitions
- Smart Home Integration
- IoT Remote Control

---

# Components Used

| Component | Description |
|---|---|
| ESP32 DevKit V1 | Main controller |
| OLED Display SSD1306 | Real-time system display |
| PIR Motion Sensor | Motion detection |
| LDR Sensor | Ambient light sensing |
| RGB LED (Common Anode) | Lighting and status indication |
| Push Button | Manual control |
| Breadboard | Circuit assembly |
| Jumper Wires | Electrical connections |
| Resistors | RGB LED protection |

---

# Pin Connections

| Component | ESP32 Pin |
|---|---|
| RGB Red | GPIO14 |
| RGB Green | GPIO26 |
| RGB Blue | GPIO13 |
| PIR Sensor OUT | GPIO27 |
| LDR Sensor AO | GPIO34 |
| OLED SDA | GPIO32 |
| OLED SCL | GPIO33 |
| Push Button | GPIO25 |

---

# RGB Lighting Modes

| Mode | Color | Description |
|---|---|---|
| Bright Environment | OFF | Enough ambient light detected |
| Dark without Motion | Blue | Energy-saving night mode |
| Dark with Motion | White | Motion detected |
| MANUAL ON MODE | Green | User manually activated system |
| MANUAL OFF MODE | Red | User manually disabled system |

---

# Operating Modes

## AUTO MODE

The system operates fully automatically:

- The LDR sensor measures brightness.
- The PIR sensor detects motion.
- The RGB lighting automatically reacts to environmental conditions.

---

## MANUAL ON MODE

- The RGB lighting is manually activated.
- The RGB LED glows green continuously.
- Sensor values are ignored.

---

## MANUAL OFF MODE

- The system is manually disabled.
- The RGB LED glows red.
- Automatic functions are disabled.

---

# OLED Display Functions

The OLED display shows real-time information:

- Current operating mode
- Light sensor values
- Motion status
- RGB status
- System information

This allows local system monitoring directly from the hardware.

---

# WiFi Web Dashboard

The project includes a modern WiFi web dashboard.

Dashboard features:

- Live system data display
- Full operating mode control
- Smartphone remote access
- ESP32 restart function
- User-friendly interface
- Real-time synchronization

---

# System Logic

1. The system connects to WiFi.
2. The ESP32 starts a local web server.
3. Sensor values are continuously monitored.
4. The OLED display updates live information.
5. The RGB lighting reacts automatically based on brightness and movement.
6. Users can control the system remotely through the dashboard.
7. All system states are synchronized in real time.

---

# Practical Applications

This project can be used in many real-life applications:

- Smart Home lighting systems
- Energy-efficient room automation
- Automatic night lighting
- IoT-based building automation
- Intelligent smart-building systems
- Embedded and IoT learning platforms
- Smart energy system prototypes
- Security lighting systems
- Intelligent hallway lighting
- Garage automation
- Motion-based lighting systems
- Smart City applications
- Industrial monitoring systems

---

# Technologies Used

- ESP32 Microcontroller
- MicroPython
- Embedded Systems
- WiFi Networking
- IoT Systems
- PWM RGB Control
- Sensor Integration
- OLED Display Communication
- Web Server Programming
- Smart Home Automation

---

# Required Libraries

```python
import network
import socket
import machine
import time
import ssd1306
```

Additionally, the `ssd1306.py` file must be uploaded to the ESP32 board.

---

# Full MicroPython Source Code

```python
# Full ESP32 Smart Room Controller V3 Source Code
# OLED + WiFi Dashboard + RGB + PIR + LDR + Web Control
```

---

# Developer

## Ahmad Azroun

Renewable Energy Manager | IoT & Smart Energy Systems Developer
