import requests
from transportation import Transportation
from leg import Leg


class Pedestrian(Transportation):

    def _get_itinerary(self):
        url = self.url_here_routing_api('pedestrian')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        mode = {'type': 'pedestrian'}
        leg = Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])
        return [leg]


if __name__ == '__main__':
    print('********TRAJET A PIED**********')
    journey = Pedestrian((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.get_itinerary())
