import requests

from transportation import Transportation
from pedestrian import Pedestrian
from bike import Bike


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
        resp = requests.get(url)
        data = resp.json()['records']
        if not data:
            print('Pas de vélib dispos')
        else:
            data = data[0]['fields']['geo']
            return data[0], data[1]

    def get_closest_public_bike_terminal_destination(self):
        url = self.url_destination_terminal_public_bike_api()
        resp = requests.get(url)
        data = resp.json()['records']
        if not data:
            print('Impossible de reposer le velib à proximité')
        else:
            data = data[0]['fields']['geo']
            return data[0], data[1]

    def _get_itinerary(self):
        # Get the origin and destination terminal
        # Have to abort if there are no close public bike terminal at the origin / destination
        origin_borne = self.get_closest_public_bike_terminal_origin()
        destination_borne = self.get_closest_public_bike_terminal_destination()
        pedestrian_origin = Pedestrian(self.origin, origin_borne).itinerary
        bike_travel = Bike(origin_borne, destination_borne).itinerary
        pedestrian_destination = Pedestrian(destination_borne, self.destination).itinerary
        return (pedestrian_origin + bike_travel + pedestrian_destination).legs


if __name__ == '__main__':
    journey = PublicBike((48.871192, 2.351512), (48.840137, 2.351407))
    print(journey.itinerary.legs)
