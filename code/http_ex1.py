import m5wifi
import m5config
import urequests

# Connexion au réseau wifi
m5wifi.connect( m5config.get_config('ssid'), m5config.get_config('passwd'), affiche_configuration=False )

req = urequests.get( "http://blended.mips.science/" )
print( req.text )
