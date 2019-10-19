import requests
from leg import Leg
from transportation import Transportation

class Scooter(Transportation):

    def _get_itinerary(self):
        url = self.url_here_routing_api('bicycle')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        mode = {'type': 'scooter'}
        return [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])]


if __name__ == '__main__':
    journey = Scooter((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary)