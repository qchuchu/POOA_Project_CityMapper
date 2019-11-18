from views import app
from itinerary import Itinerary
import requests

def get_request(url):
    try:
        resp = requests.get(url)
    except requests.ConnectionError:
        print("Please Check your internet connection !")
        return [None, "connection error"]
    stat = ""
    stat_code = resp.status_code
    if stat_code == 200:
        stat = "successful"
    else:
        stat = "request failed, please check url"
        if stat_code == 401:
            stat += " : unidentified user"
        if stat_code == 403:
            stat += " : refused access"
        if stat_code == 404:
            stat += " : not found"
        if stat_code in [500, 503, 504]:
            stat += " : servor did not answered"
    return [resp, stat]


class Transportation:

    def __init__(self, origin, destination):
        self._origin = origin
        self._destination = destination
        itinerary_response = self._get_itinerary()
        self._itinerary = Itinerary(origin, destination, itinerary_response[0], itinerary_response[1])
        self._legit = itinerary_response[1]

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def itinerary(self):
        return self._itinerary

    @property
    def legit(self):
        return self._legit

    def is_legit(self):
        if self._legit[0] == 0:
            return False
        else:
            return True

    # Abstract Method to be overriden in the children classes. The get_itinerary should return a list of legs.
    def _get_itinerary(self):
        pass

    def url_here_routing_api(self, transport_mode):
        """
        This function returns the URL to make personalized API Calls on Here
        :param transport_mode:
        :param origin: Origin GPS Coordinates, tuple shaped
        :param destination: Destination GPS Coordinates, tuple shaped
        :return: url string
        """

        base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
        app_id = "?app_id=" + app.config['APP_ID']
        app_code = "&app_code=" + app.config['APP_CODE']
        origin = "&waypoint0=geo!{},{}".format(self._origin[0], self._origin[1])
        destination = "&waypoint1=geo!{},{}".format(self.destination[0], self.destination[1])
        if transport_mode == 'public':
            mode = "&departure=now&mode=fastest;publicTransport&combineChange=true"
        else:
            mode = "&mode=fastest;" + transport_mode
        language = "&language=fr-fr"
        return base + app_id + app_code + origin + destination + mode + language