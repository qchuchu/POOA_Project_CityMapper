import requests

from transportation import Transportation
from pedestrian import Pedestrian
from scooter import Scooter
from views import app

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

    def _get_itinerary(self):
        legit = (1 , 'legit itinerary')
        try:
            scooter = self.get_closest_scooter()
            scooter_location = scooter['lat'], scooter['lng']
        except:
            legit = (0, 'no scooter found')
            return ([], legit)
        pedestrian_origin = Pedestrian(self.origin, scooter_location).itinerary
        scooter_travel = Scooter(scooter_location, self.destination).itinerary
        scooter_travel.legs[0].mode = {'type': 'scooter', 'provider': scooter['provider']}
        # We suppose that we can leave the Lime
        final = pedestrian_origin + scooter_travel
        return final.legs

if __name__ == '__main__':
    print('********TRAJET A LIME**********')
    journey = PublicScooter((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary.legs)