import requests
from transportation_api.transportation import Transportation, get_request
from transportation_api.leg import Leg


class Car(Transportation):
    """
    Class that makes the API call to HERE and return the itinerary by Car
    """

    def _get_itinerary(self):
        legit = (1, "legit itinerary")
        url = self.url_here_routing_api('car')
        response, status = get_request(url)
        if status != "successful":
            legit = (0, status)
            return [], legit
        else:
            try:
                data = response.json()['response']['route'][0]['summary']
            except KeyError as e:
                return [], (0, 'error parsing data')
            mode = {'transport_mode': 'car'}
        price = data['distance'] / 1000 * 1.6 * (6 / 100)
        car_leg = [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'], price)]
        return "car", car_leg, legit

