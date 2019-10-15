import requests

from gpsapp.transportation import Transportation
from gpsapp.pedestrian import Pedestrian
from gpsapp.scooter import Scooter

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


class PublicScooter(Transportation):

    def get_closest_scooter(self):
        api_url_base = 'https://api.multicycles.org/v1'
        headers = {'content-type': 'application/json'}
        params = {'access_token': app.config['ACCESS_TOKEN_SCOOTER']}
        position = {"lat": self._origin[0], "lng": self._origin[1]}
        resp = requests.post(api_url_base,
                             json={'query': scooter_query, 'variables': position},
                             params=params,
                             headers=headers).json()
        return resp['data']['vehicles'][0]

    def get_itinerary(self):
        scooter = self.get_closest_scooter()
        scooter_location = scooter['lat'], scooter['lng']
        pedestrian_origin = Pedestrian(self._origin, scooter_location).get_itinerary()
        scooter_travel = Scooter(scooter_location, self._destination).get_itinerary()
        # We suppose that we can leave the Lime
        return pedestrian_origin + scooter_travel
