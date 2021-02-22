import m5wifi
import m5config
import urequests

def get_api_data():
    # Documentation de l'API
    # https://openweathermap.org/current#current_JSON

    # Connexion au réseau wifi
    m5wifi.connect( get_config('ssid'), get_config('passwd') )

    # Lecture de la clé de l'API
    api_key = m5config.get_config('openweathermapApiKey')

    url_api = "http://api.openweathermap.org/data/2.5/weather?id=2980291&units=metric&appid=" + api_key

    # Executer la requete
    req = urequests.get( url_api )
    api_data = req.json()

    return(api_data)

def get_meteo( api_data ):
    meteo = {}
    meteo['meteo'] = api_data["weather"][0]["description"]
    meteo['lieu'] = api_data["name"]
    meteo['coord_lon'] = api_data["coord"]["lon"]
    meteo['coord_lat'] = api_data["coord"]["lat"]
    meteo['vent_kph'] = api_data["wind"]["speed"] * 3.6
    meteo['vent_dir'] = api_data["wind"]["deg"]
    meteo['temp_ressentie'] = api_data["main"]["feels_like"]
    meteo['temperature'] = api_data["main"]["temp"]
    meteo['humidite'] = api_data["main"]["humidity"]
    meteo['pression'] = api_data["main"]["pressure"]

    return( meteo )

# Requete API openweathermap.org
api_data = get_api_data()

# Afficher les données recues de l'API
print( "Affichage des donnees brutes" )
print( api_data )

# Mise en forme des données de l'API
meteo = get_meteo( api_data )

print( "\nMeteo:" )
for param in meteo:
    print( "\t", param, "=", meteo[param] )
