import requests
from gpsapp.transportation import Transportation


class Car(Transportation):
    """
    Class that makes the API call to HERE and return the itinerary by Car
    """

    def get_itinerary(self):
        url = self.url_here_routing_api('car')
        data = requests.get(url).json()['response']['route'][0]['summary']
        self.itinerary.distances.append(data['distance'])
        self.itinerary.times.append(data['travelTime'])
        self.itinerary.modes.append('Car')
        return self.itinerary


if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    car = Car(massy, eiffel)
    print(car.get_itinerary())

