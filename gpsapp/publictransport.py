import requests
from gpsapp.transportation import Transportation


class PublicTransport(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('public')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['leg'][0]['maneuver']
        # Show the steps related to Public Transportation
        public_data = [x for x in data if x['_type'] == 'PublicTransportManeuverType']
        # Show the steps related to Foot Steps
        foot_data = [x for x in data if x['_type'] != 'PublicTransportManeuverType']
        return foot_data


"""try:
    assert resp.status_code == 200
    print('Ceci est la réponse')
    print(resp.json())
except AssertionError:
    print("API Call didn't work")"""



