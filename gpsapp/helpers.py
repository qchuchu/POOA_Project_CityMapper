# Ce fichier contient des fonctions communes aux différentes classes,
# facilitant la lisibilité du code

import os
# Pour accéder aux APP_ID et aux APP_CODE, il faut utiliser l'os.environ
import requests
# Pour faire des requêtes get
from gpsapp.views import app

def url_here_routing_api(origin, destination):
    """
    Cette fonction retourne l'URL nécessaire pour faire des requêtes GET à l'API Here
    :param waypoint0: Coordonnées GPS de départ, sous forme de tuples de string
    :param waypoint1: Coordonnées GPS de d'arrivée, sous forme de tuples de string
    :return:
    """

    base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
    app_id = "?app_id=" + app.config['APP_ID']
    app_code = "&app_code=" + app.config['APP_CODE']
    origin = "&waypoint0=geo!" + ",".join(origin)
    destination = "&waypoint1=geo!" + ",".join(destination)
    mode = "&mode=fastest;car;traffic:disabled"
    language = "&language=fr-fr"
    return base + app_id + app_code + origin + destination + mode + language

def url_here_weather_api():
    base = 'https://weather.api.here.com/weather/1.0/report.xml'
    app_id = "?app_id=" + app.config['APP_ID']
    app_code = "&app_code=" + app.config['APP_CODE']
    product = "&product=observation"
    name = "&name=Paris"
    return base + app_id + app_code + product + name

scooter_query = """
query ($lat: Float!, $lng: Float!) {
    vehicles (lat: $lat, lng: $lng, typeVehicles: [SCOOTER]) {
        type
        lat
        lng
        provider {
            name
        }
    }
}
"""


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    url = url_here_routing_api(massy, eiffel)
    route = requests.get(url).json()
    print(url)
