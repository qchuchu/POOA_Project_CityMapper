import requests
import json
import os
from pedestrian import *
from bike import *

class Velib:

    """Cette classe permet de déterminer un trajet en velib pour l'utilisateur"""

#on prend quatre attributs en entrée qui sont la latitude et la longitude de départ; latitude et longitude d'arrivée, sous forme de string

    def __init__(self, latdep, longdep, latarrival, longarrival):
        self.latdep = latdep
        self.longdep = longdep
        self.latarrival = latarrival
        self.longarrival = longarrival

    def get_velib(self):
        url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1&facet=station_state&facet=nbbike&refine.station_state=Operative&exclude.nbbike=0&geofilter.distance='+self.latdep+'%2C+'+self.longdep+'%2C+1000'
#elles sont ordonnées par distance donc prendre la première c'est prendre la plus proche
# pour l'instant on va regarder que les stations dans un rayon de 1km
# amelioration = regarder les ebike et regarder ou on peut prendre l'abonnement (ce sera des données d'entrée)
        resp=requests.get(url)
        data=resp.json()
        if data['records']==[]:
            print('Pas de vélib dispos')
        else :
            lat_stat_dep = data['records'][0]['fields']['geo'][0]
            long_stat_dep = data['records'][0]['fields']['geo'][1]
            return str(lat_stat_dep) + ',' + str(long_stat_dep)


    def return_velib(self):
        url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1&facet=nbfreedock&facet=station_state&refine.station_state=Operative&exclude.nbfreedock=0&geofilter.distance='+self.latarrival+'%2C+'+self.longarrival+'%2C+1000'
        resp=requests.get(url)
        data=resp.json()
        if data['records']==[]:
            print('Impossible de reposer le vélib à proximité')
        else:
            lat_stat_return = data['records'][0]['fields']['geo'][0]
            long_stat_return = data['records'][0]['fields']['geo'][1]
            return str(lat_stat_return)+','+str(long_stat_return)


    def itinerary(self):

        step1 = Pedestrian(self.latdep+','+self.longdep,Velib.get_velib(self))
        step2 = Bike(Velib.get_velib(self),Velib.return_velib(self))
        step3 = Pedestrian(Velib.return_velib(self),self.latarrival+','+self.longarrival)
        print (Pedestrian.journey(step1), Bike.journey(step2), Pedestrian.journey(step3))

trajet = Velib('48.881','2.2956199999999853','48.8718','2.2932799999999816')
trajet.itinerary()











