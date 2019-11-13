import requests
from transportation import Transportation, get_request
from leg import Leg


class Pedestrian(Transportation):

    def _get_itinerary(self):
        legit = (1, 'legit itinerary')
        url = self.url_here_routing_api('pedestrian')
        response, status = get_request(url)
        if status != "successful":
            legit = (0, status)
            return [], legit
        else:
            try:
                data = response.json()['response']['route'][0]['summary']
            except KeyError as e:
                legit = (1, "error parsing data")
                return [], legit
        mode = {'transportMode': 'pedestrian'}
        return [Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])], legit


if __name__ == '__main__':
    print('********TRAJET A PIED**********')
    journey = Pedestrian((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary)
