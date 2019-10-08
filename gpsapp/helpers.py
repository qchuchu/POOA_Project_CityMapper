# Ce fichier contient des fonctions communes aux différentes classes,
# facilitant la lisibilité du code

import os
# Pour accéder aux APP_ID et aux APP_CODE, il faut utiliser l'os.environ
import requests
# Pour faire des requêtes get

def url_here_routing_api(waypoint0, waypoint1):
    """
    Cette fonction retourne l'URL nécessaire pour faire des requêtes GET à l'API Here
    :param waypoint0: Coordonnées GPS de départ, sous forme de tuples de string
    :param waypoint1: Coordonnées GPS de d'arrivée, sous forme de tuples de string
    :return:
    """

    base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
    app_id = "?app_id=" + os.environ['APP_ID']
    app_code = "&app_code=" + os.environ['APP_CODE']
    waypoint0 = "&waypoint0=geo!" + ",".join(waypoint0)
    waypoint1 = "&waypoint1=geo!" + ",".join(waypoint1)
    mode = "&mode=fastest;car;traffic:disabled"
    language = "&language=fr-fr"
    return base + app_id + app_code + waypoint0 + waypoint1 + mode + language

def url_here_weather_api():
    base = 'https://weather.api.here.com/weather/1.0/report.xml'
    app_id = "?app_id=" + os.environ['APP_ID']
    app_code = "&app_code=" + os.environ['APP_CODE']
    product = "&product=observation"
    name = "&name=Paris"
    return base + app_id + app_code + product + name

def url_here_public_transport_api():
    base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
    app_id = '?app_id=djGZJjsUab93vV3VqBKA'
    app_code = '&app_code=u3bReKn8wIAuZl74j1iyGA'
    mode = "&departure=now&mode=fastest;publicTransport&combineChange=true"
    waypoint0 = '&waypoint0=geo!' + ",".join(waypoint0)
    waypoint1 = '&waypoint1=geo!' + ",".join(waypoint1)
    return  base + app_id + app_code + waypoint0 + waypoint1 + mode

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
