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


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    url = url_here_routing_api(massy, eiffel)
    route = requests.get(url).json()
    print(url)

