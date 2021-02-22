# TP - Communications WIFI / API REST / MQTT / ESPNOW / BlueTooth

Codes sources disponibles dans le dossier code/

## Connexion réseau WIFI

documentation module network <https://micropython-docs-esp32.readthedocs.io/en/esp32_doc/library/network.WLAN.html>

- crée un objet station reseau WLAN
- active l'interface réseau
- connexion au réseau wifi
- vérifie si la connexion est active
- déconnexion
- scanner les réseaux wifi disponibles
- récupérer la configuration IP

```python
import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
wifi.isconnected()
wifi.disconnect()
wifi.scan()
wifi.ifconfig()
```
Connexion au réseau Wifi, fichier code/m5wifi.py

Généralités sur réseau wifi <https://sourcedaddy.com/networking/wireless-networking.html>

## HTTP - Lecture site web M5stack.com
source http_ex1.py

## HTTP - Connexion API openweathermap.org
source http_openweathermap.py

## Mini appli météo
source meteo.py

## Utilisation MQTT
source tuto_mqtt_sub.py

## Utilisation bluetooth BLE

## Utilisation NTP

## Connexion socket
Unix sockets en langage C <https://www.tutorialspoint.com/unix_sockets/socket_core_functions.htm>

## Utilisation ESPNOW
