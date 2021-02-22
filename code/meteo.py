import http_openweathermap
from m5stack import *
from m5ui import *

def print_align_droite( decalage, y, texte ):
    x_debut = 320 - decalage - lcd.textWidth(texte)
    lcd.text(x_debut, y, texte)
    return

lcd.clear()

# recuoeration des données de l'API
meteo = http_openweathermap.get_meteo( get_api_data() )

lcd.font(lcd.FONT_DejaVu24)
lcd.text(20, 60, "meteo")
print_align_droite( 20, 60, meteo['meteo'] )

lcd.text(20, 120, "temperature")
print_align_droite( 20, 120, str(meteo['temperature']) )

lcd.text(20, 180, "humidite")
print_align_droite( 20, 180, str(meteo['humidite']) )
