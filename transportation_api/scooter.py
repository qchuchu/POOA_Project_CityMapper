from transportation_api.leg import Leg
from transportation_api.transportation import Transportation, get_request


class Scooter(Transportation):

    def _get_itinerary(self):
        legit = (1, 'legit itinerary')
        url = self.url_here_routing_api('bicycle')
        response, status = get_request(url)
        if status != "successful":
            legit = (0, status)
            return [], legit
        else:
            try:
                data = response.json()['response']['route'][0]['summary']
            except KeyError as e:
                legit = (0, "error in parsing data")
                return [], legit
            mode = {'transport_mode': 'scooter'}
        return "scooter", [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])], legit


if __name__ == '__main__':
    journey = Scooter((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey._get_itinerary())