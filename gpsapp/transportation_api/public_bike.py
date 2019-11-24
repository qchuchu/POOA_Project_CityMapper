from transportation_api.transportation import Transportation, get_request
from transportation_api.pedestrian import Pedestrian
from transportation_api.bike import Bike


class PublicBike(Transportation):
    """
    This Class Object looks for the possibility to rent a public bike
    """

    def url_origin_terminal_public_bike_api(self):
        base = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1' \
               '&facet=station_state&facet=nbbike&refine.station_state=Operative&exclude.nbbike=0&geofilter.distance= '
        return "{}{}%2C{}%2C+1000".format(base, self._origin[0], self._origin[1])

    def url_destination_terminal_public_bike_api(self):
        base = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1' \
               '&facet=nbfreedock&facet=station_state&refine.station_state=Operative&exclude.nbfreedock=0&geofilter' \
               '.distance= '
        return "{}{}%2C{}%2C+1000".format(base, self._destination[0], self._destination[1])

    def get_closest_public_bike_terminal_origin(self):
        # Return something
        url = self.url_origin_terminal_public_bike_api()
        response, status = get_request(url)
        if status != "successful":
            return status
        else:
            try:
                data = response.json()['records'][0]['fields']['geo']
            except (IndexError, KeyError) as e:
                return e
        return data[0], data[1]

    def get_closest_public_bike_terminal_destination(self):
        url = self.url_destination_terminal_public_bike_api()
        response, status = get_request(url)
        if status != "successful":
            return status
        else:
            try:
                data = response.json()['records'][0]['fields']['geo']
            except (KeyError, IndexError) as e:
                return e
        return data[0], data[1]

    def _get_itinerary(self):
        origin_borne = self.get_closest_public_bike_terminal_origin()
        try:
            assert (type(origin_borne) == tuple)
        except AssertionError as e:
            return [], (0, origin_borne)

        destination_borne = self.get_closest_public_bike_terminal_destination()
        try:
            assert (type(destination_borne) == tuple)
        except AssertionError as e:
            return [], (0, destination_borne)

        pedestrian_origin = Pedestrian(self.origin, origin_borne)
        try:
            assert (pedestrian_origin.legit == (1, "legit itinerary"))
        except AssertionError as e:
            return [], pedestrian_origin.legit

        bike_travel = Bike(origin_borne, destination_borne)
        try:
            assert (bike_travel.legit == (1, "legit itinerary"))
        except AssertionError as e:
            return [], bike_travel.legit
        bike_travel.itinerary.legs[0].mode = {'transport_mode': 'publicBike', 'provider': 'Velib'}
        pedestrian_destination = Pedestrian(destination_borne, self.destination)
        try:
            assert (pedestrian_destination.legit == (1, "legit itinerary"))

        except AssertionError as e:
            return [], pedestrian_destination.legit

        # Set up the price 
        bike_travel.itinerary.legs[0].price = 1 + bike_travel.itinerary.legs[0].duration // (30*60)

        itinerary = pedestrian_origin.itinerary + bike_travel.itinerary + pedestrian_destination.itinerary

        return "publicBike", itinerary.legs, (1, "legit itinerary")

