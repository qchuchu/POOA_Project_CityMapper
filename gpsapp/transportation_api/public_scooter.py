import requests
from transportation_api.transportation import Transportation
from transportation_api.pedestrian import Pedestrian
from transportation_api.scooter import Scooter

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

ACCESS_TOKEN_SCOOTER = '0E4emOhyC3gS3LOnDcmiQDZs1bbXb1US'


class PublicScooter(Transportation):

    def get_closest_scooter(self):
        api_url_base = 'https://api.multicycles.org/v1'
        headers = {'content-type': 'application/json'}
        params = {'access_token': ACCESS_TOKEN_SCOOTER}
        position = {"lat": self._origin[0], "lng": self._origin[1]}
        resp = requests.post(api_url_base,
                             json={'query': scooter_query, 'variables': position},
                             params=params,
                             headers=headers).json()
        return resp['data']['vehicles'][0]

    def _get_itinerary(self):
        legit = (1, 'legit itinerary')
        try:
            scooter = self.get_closest_scooter()
            scooter_location = scooter['lat'], scooter['lng']
        except IndexError as e:
            legit = (0, 'no scooter found')
            return [], legit
        # Calculate the walking part to the Scooter
        pedestrian_origin = Pedestrian(self.origin, scooter_location).itinerary
        # Calculating the itinerary from Scooter to Endpoint
        scooter_travel = Scooter(scooter_location, self.destination).itinerary
        scooter_travel.legs[0].mode = {'transport_mode': 'scooter', 'provider': scooter['provider']['name']}
        # A Lime is 1 euro + 0.20 euro per minute
        scooter_travel.legs[0].price = 1 + scooter_travel.legs[0].duration/60*0.2
        # We suppose that we can leave the Lime anywhere
        final = pedestrian_origin + scooter_travel
        return "publicScooter", final.legs, legit