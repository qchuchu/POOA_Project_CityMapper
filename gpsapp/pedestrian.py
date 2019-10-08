import requests
import json
import os
from gpsapp.views import app

class Pedestrian:

    def __init__(self, departure, arrival):
        self.departure = departure
        self.arrival = arrival

    def journey(self):
        base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
        app_id = '?app_id=' + app.config['APP_ID]
        app_code = '&app_code=' + app.config['APP_CODE']
        mode = '&mode=fastest;pedestrian'
        waypoint0 = '&waypoint0=geo!' + self.departure
        waypoint1 = '&waypoint1=geo!' + self.arrival
        final = base+app_id+app_code+waypoint0+waypoint1+mode
        resp = requests.get(final)
        data = resp.json()
        print('La distance à parcourir est de {} mètres' .format(data['response']['route'][0]['summary']['distance']))
        print('Vous mettrez {} secondes pour arriver à destination' .format(data['response']['route'][0]['summary']['travelTime']))


#trajet1=Pedestrian('48.881,2.2956199999999853', '48.8586,2.284249999999929')
#trajet1.journey()

