# Plan TP M5Stack - BACH TECH

## Séance 1 - présentation installation

- présentation
  - les gammes de micro-controlleurs (Arduino, STM32, ESP8266, ESP32, Raspberry pico, Raspberry.)
  - panorama performances / connectivité / applications / langages de développement
- M5 Stack
  - gamme basic, core2, M5Paper, atomU, M5Go, M5StickC, M5Stack Tough
  - caractéristiques techniques
    * Communication
        * LoRa/LoRaWAN
        * GPS satellite positioning module
        * GSM stackable 2G communication module, LTE
        * NB-IoT wireless communication
        * I2C / CAN / RS485 / TTL Interface
    * Driver
        * three-axis stepper motor driver module
        * servo driver module
        * DC MOTOR module
        * FAN Module
    * Extension
        * 750mAh High-Capacity Battery
        * universal prototype perboard
        * USB Module
        * M-BUS
        * Hardwired TCP/IP embedded Ethernet / Power Over Ethernet
        * Camera
        * image recognition development board
        * AI Camera / machine vision capabilities
    * Faces / Hat
        * FACES Keyboard(GameBoy, Calculator, QWERTY, Calculator)
        * ENCODER Module
        * JOYSTICK
        * finger-print recognition
        * RFID panel
        * THERMAL CAMERA
        * ADC / DAC
        * IR sensor

- présentation UIFlow
  
- Installation, paramétrage
  - Download / Install CP2104 driver
  - Download / Install M5burner
  - Firmware burning (UIFlow)
  - UIFlow desktop + connexion USB
  - connexion wifi (tux)
- Prise en main

## Séance 2 - premiers pas

- premières fonctions :  label, graphique, image, animations, sons, couleurs...
- notions script: setup, loop, conditions, variables
- événements : touches, timer
- mise en oeuvre capteur PIR Grove

## Séance 3 - Du microcontrolleur au serveur MQTT + SQL

- Présentation MQTT (broker, publish, subscribe)
- Broker MQTT perso: mqtt.mips.science:1883
- envoi état capteurs PIR sur broker MQTT sur topic "alarme"
- réception de messages MQTT du topic "alarme"
- script serveur d'affichage des messages (mosquitto_sub, module mqtt + python3)
- script serveur de sauvegarde des alarmes dans BDD SQLlite

## Séance 4 - Utilisation API

- Connexion réseau WIFI
- Utilisation d'une API "hello world" (python3 + fastAPI)
- Utilisation de API openweather (script en micro python)
- Affichage de la météo sur M5Stack