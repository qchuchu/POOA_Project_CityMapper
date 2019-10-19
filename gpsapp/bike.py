import requests
from transportation import Transportation
from leg import Leg


class Bike(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('bicycle')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        mode = {'type': 'bike'}
        return [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])]


if __name__ == '__main__':
    journey = Bike((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.get_itinerary())













