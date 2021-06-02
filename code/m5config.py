import ujson
import os

# verifie l'existence du fichier /flash/config.json
def exist_config_file():
    existe = False

    files = os.listdir('/flash')
    if 'config.json' in files:
        existe = True

    return( existe )

# Lecture de la configuration dans /flash/config.json
def read_config_file():

    config = {}
    if exist_config_file():
        with open('/flash/config.json') as fichier:
            config = ujson.load(fichier)

    return( config )

# Ecriture de la config /flash/config.json
def write_config_file( config ):
    with open('/flash/config.json', 'w') as fichier:
        ujson.dump(config, fichier)

    return

def get_config( param ):
    config = read_config_file()
    val = ""
    if param in config:
        val = config[param]

    return( val )

def set_config( param, val ):
    config = read_config_file()
    config[param] = val
    write_config_file( config )
    return( True )

def del_config( param ):
    config = read_config_file()
    del config[param]
    write_config_file( config )
    return( True )
