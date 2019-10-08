# Ce fichier contient des fonctions communes aux différentes classes,
# facilitant la lisibilité du code

import os
# Pour accéder aux APP_ID et aux APP_CODE, il faut utiliser l'os.environ
import requests
# Pour faire des requêtes get
from gpsapp.views import app





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
