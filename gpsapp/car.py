import requests
from transportation import Transportation, get_request
from leg import Leg


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
            mode = {'transportMode': 'car'}
        return [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])], legit


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    car = Car(massy, eiffel)
    print(car._get_itinerary())

