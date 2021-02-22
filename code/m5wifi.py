import time
import network

# Connect to a specific wifi network
def connect(ssid, password, timeout=30000, affiche_configuration=False):
    # initialisation Wifi en mode station
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)    # Connexion

    # Attente que la connexion soit effective
    t = time.ticks_ms()
    timeout_error = False
    while not wifi.isconnected() and not timeout_error:
        if time.ticks_diff(time.ticks_ms(), t) > timeout:
            timeout_error = True

    if not wifi.isconnected():
        connexion_active = False
        wifi.disconnect()
        if timeout_error:
            print("wifi: timeout. impossible de se connecter")
        else:
            print("wifi: impossible de se connecter")
    else:
        connexion_active = True
        if affiche_configuration:
            print_config()

    return(connexion_active)


def disconnect():
    wifi = network.WLAN(network.STA_IF)
    wifi.disconnect()


def isconnected():
    wifi = network.WLAN(network.STA_IF)
    return wifi.isconnected()


def ifconfig():
    wifi = network.WLAN(network.STA_IF)
    config = {}
    config['ip'], config['subnetmask'], config['gateway'], config['dns'] = wifi.ifconfig()

    return( config )

def wificonfig():
    config = {}
    config['rssi'] = wifi.status('rssi')
    config['mac'] = ubinascii.hexlify( wifi.config('mac') )
    config['ssid'] = wifi.config('essid')
    config['dhcp_hostname'] = wifi.config('dhcp_hostname')

    return( config )


def print_config():
    # Affichage de la configuration Wifi
    print( "Wifi config:" )
    config = wificonfig()
    for param in config:
        print( "\t", param, "=", config[param] )

    # Affichage de la configuration IP
    print( "\nIP config:" )
    config = ifconfig()
    for param in config:
        print( "\t", param, "=", config[param] )

    return

def scan():
    scanlist = wifi.scan()

    wlanlist = []
    for wlan in scanlist:
        wlanlist.append( {  'ssid': wlan[0].decode('utf-8'),
                            'channel': wlan[2],
                            'RSSI': wlan[3],
                            'authmode': authmode_desc( wlan[4] ),
                            'hidden': wlan[5] } )
    return( wlanlist )

def authmode_desc( authmode ):
    auth_desc = ""

    if authmode == 0:
        auth_desc = 'open'
    elif authmode == 1:
        auth_desc = 'WEP'
    elif authmode == 2:
        auth_desc = 'WPA-PSK'
    elif authmode == 3:
        auth_desc = 'WPA2-PSK'
    elif authmode == 4:
        auth_desc = 'WPA/WPA2-PSK'
    else:
        auth_desc = str( wlan[4] )

    return( auth_desc )
