from transportation_api.transportation import Transportation, get_request
from transportation_api.leg import Leg


class Pedestrian(Transportation):

    def _get_itinerary(self):
        legit = (1, 'legit itinerary')
        url = self.url_here_routing_api('pedestrian')
        response, status = get_request(url)
        if status != "successful":
            legit = (0, status)
            return [], legit
        else:
            try:
                data = response.json()['response']['route'][0]['summary']
            except KeyError as e:
                legit = (1, "error parsing data")
                return [], legit
        mode = {'transport_mode': 'pedestrian'}
        return "pedestrian", [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])], legit