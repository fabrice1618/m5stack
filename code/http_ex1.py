import m5wifi
import m5config
import urequests

# Connexion au réseau wifi
connect( get_config('ssid'), get_config('passwd'), affiche_configuration=True )

req = urequests.get( "https://m5stack.com/" )
print( req.text )
