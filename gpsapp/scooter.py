import requests
from gpsapp.helpers import scooter_query
from gpsapp.views import app


class Scooter:

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    @property
    def get_closest_scooter(self):
        api_url_base = 'https://api.multicycles.org/v1'
        headers = {'content-type': 'application/json'}
        params = {'access_token': app.config['ACCESS_TOKEN_SCOOTER']}
        position = {"lat": self.origin[0], "lng": self.origin[1]}
        resp = requests.post(api_url_base,
                             json={'query': scooter_query, 'variables': position},
                             params=params,
                             headers=headers).json()
        return resp['data']['vehicles'][0]

    def get_itinerary(self):
        scooter = self.get_closest_scooter

        pass


if __name__ == '__main__':
    scooter = Scooter((48.880960, 2.295620), (48.880960, 2.295620))
    print(scooter.get_closest_scooter)

