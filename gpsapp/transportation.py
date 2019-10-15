from gpsapp.views import app
from gpsapp.itinerary import Itinerary


class Transportation:

    def __init__(self, origin, destination):
        self._origin = origin
        self._destination = destination
        self._itinerary = Itinerary(origin, destination)

    @property
    def itinerary(self):
        return self._itinerary

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
        destination = "&waypoint1=geo!{},{}".format(self._destination[0], self._destination[1])
        if transport_mode == 'public':
            mode = "&departure=now&mode=fastest;publicTransport&combineChange=true"
        else:
            mode = "&mode=fastest;" + transport_mode
        language = "&language=fr-fr"
        return base + app_id + app_code + origin + destination + mode + language

