import requests
from gpsapp.transportation import Transportation
from leg import Leg


class Car(Transportation):
    """
    Class that makes the API call to HERE and return the itinerary by Car
    """

    def _get_itinerary(self):
        url = self.url_here_routing_api('car')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        mode = {'type': 'car'}
        leg = Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])
        self.itinerary.add(leg)
        return self.itinerary


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    car = Car(massy, eiffel)
    print(car.get_itinerary())

