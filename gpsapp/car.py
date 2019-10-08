from gpsapp.helpers import url_here_routing_api
import requests

class Car:
    """Cette classe retournera un objet itinéraire qui donnera des informations
    sur un trajet en voiture entre deux positions GPS
    """

    def __init__(self, waypoint0, waypoint1):
        self._waypoint0 = waypoint0
        self._waypoint1 = waypoint1

    def get_itinerary(self):
        url = url_here_routing_api(self._waypoint0, self._waypoint1)
        data = requests.get(url).json()['response']['route'][0]['summary']
        distance = data['distance'] / 1000



if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    car = Car(massy, eiffel)
    print(car.get_itinerary())

