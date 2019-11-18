import requests
from transportation import Transportation, get_request
from leg import Leg


class Car(Transportation):
    """
    Class that makes the API call to HERE and return the itinerary by Car
    """

    def _get_itinerary(self):
        legs = []
        legit = (1, "legit itinerary")
        url = self.url_here_routing_api('car')
        resp, stat = get_request(url)
        if stat != "successfull":
            legit = (0, stat)
            return([], legit)
        else:
            data = resp.json()['response']['route'][0]['summary']
            mode = {'type': 'car'}
            leg = Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])
            legs.append(leg)
        return (legs,legit)


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    car = Car(massy, eiffel)
    print(car._get_itinerary())

