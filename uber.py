import requests
import uber_rides
# Uber software development kit
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import os

class Uber:
    """
    Cette Class retournera un objet Itinéraire contenant la durée et le prix du transport
    """

    def __init__(self, waypoint0, waypoint1):
        self._waypoint0 = waypoint0
        self._waypoint1 = waypoint1
        self.session = Session(server_token=os.environ['TOKEN'])
        self.client = UberRidesClient(self.session)

    def get_itinerary(self):
        latitude, longitude = self._waypoint0
        response = self.client.get_products(latitude, longitude)
        products = response.json.get('products')
        return products

if __name__ == '__main__':
    massy = ('48.7228', '2.2625900000000456')
    eiffel = ('48.858370', '2.294481')
    uber = Uber(massy, eiffel)
    print(os.environ['TOKEN'])
    #print(uber.get_itinerary())


