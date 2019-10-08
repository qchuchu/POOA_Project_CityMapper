import requests
from gpsapp.views import app
from gpsapp.itinerary import Itinerary


class Transportation:

    def __init__(self, origin, destination):
        self._origin = origin
        self._destination = destination
        self._itinerary = Itinerary(origin, destination)

    @property
    def itinerary(self):
        return self._itinerary

    def url_here_routing_api(self, transport_mode):
        """
        Cette fonction retourne l'URL nécessaire pour faire des requêtes GET à l'API Here
        :param transport_mode:
        :param origin: Coordonnées GPS de départ, sous forme de tuples de string
        :param destination: Coordonnées GPS de d'arrivée, sous forme de tuples de string
        :return:
        """

        base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
        app_id = "?app_id=" + app.config['APP_ID']
        app_code = "&app_code=" + app.config['APP_CODE']
        origin = "&waypoint0=geo!{},{}".format(self._origin[0], self._origin[1])
        destination = "&waypoint1=geo!{},{}".format(self._destination[0], self._destination[1])
        if transport_mode == 'public':
            mode = "&departure=now&mode=fastest;publicTransport&combineChange=true"
        else:
            mode = "&mode=fastest;" + transport_mode
        language = "&language=fr-fr"
        return base + app_id + app_code + origin + destination + mode + language

# --------------------------------------- DIFFERENT API CALLS ---------------------------------------
class Pedestrian(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('pedestrian')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        return data
        #print('La distance à parcourir est de {} mètres'.format(data['distance']))
        #print('Vous mettrez {} secondes pour arriver à destination'.format(data['travelTime']))


class Car(Transportation):
    """Cette classe retournera un objet itinéraire qui donnera des informations
    sur un trajet en voiture entre deux positions GPS
    """

    def get_itinerary(self):
        url = self.url_here_routing_api('car')
        data = requests.get(url).json()['response']['route'][0]['summary']
        print('La distance à parcourir est de {} mètres'.format(data['distance']))
        print('Vous mettrez {} secondes pour arriver à destination'.format(data['travelTime']))


class Bike(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('bicycle')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        print('La distance à parcourir est de {} mètres'.format(data['distance']))
        print('Vous mettrez {} secondes pour arriver à destination'.format(data['travelTime']))


class PublicTransport(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('public')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        print('La distance à parcourir est de {} mètres'.format(data['distance']))
        print('Vous mettrez {} secondes pour arriver à destination'.format(data['travelTime']))


class Scooter(Transportation):

    def get_itinerary(self):
        pass


class Velib(Transportation):

    def url_velib_dispo_api(self):
        base = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1&facet=station_state&facet=nbbike&refine.station_state=Operative&exclude.nbbike=0&geofilter.distance='
        return "{}{}%2C{}%2C+1000".format(base, self._origin[0], self._origin[1])

    def url_velib_bornes_api(self):
        base = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1&facet=nbfreedock&facet=station_state&refine.station_state=Operative&exclude.nbfreedock=0&geofilter.distance='
        return "{}{}%2C{}%2C+1000".format(base, self._destination[0], self._destination[1])

    def get_closest_velib(self):
        url = self.url_velib_dispo_api()
        resp = requests.get(url)
        data = resp.json()['records']
        if not data:
            print('Pas de vélib dispos')
        else:
            data = data[0]['fields']['geo']
            return data[0], data[1]

    def get_closest_return(self):
        url = self.url_velib_bornes_api()
        resp = requests.get(url)
        data = resp.json()['records']
        if not data:
            print('Impossible de reposer le velib à proximité')
        else:
            data = data[0]['fields']['geo']
            return data[0], data[1]

    def get_itinerary(self):
        origin_borne = self.get_closest_velib()
        destination_borne = self.get_closest_return()
        step1 = Pedestrian(self._origin, origin_borne)
        step2 = Bike(origin_borne, destination_borne)
        step3 = Pedestrian(destination_borne, self._destination)
        print(step1.get_itinerary(), step2.get_itinerary(), step3.get_itinerary())

if __name__ == '__main__':
    print('********TRAJET A PIED**********')
    trajet1 = Pedestrian((48.881, 2.2956199999999853), (48.8586, 2.284249999999929))
    print(trajet1.get_itinerary())

