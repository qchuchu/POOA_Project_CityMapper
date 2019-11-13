import requests
from leg import Leg
from transportation import Transportation, get_request

class Scooter(Transportation):

    def _get_itinerary(self):
        legit = (1, 'legit itinerary')
        url = self.url_here_routing_api('bicycle')
        resp, stat = get_request(url)
        if stat != "successfull":
            legit = (0, stat)
            return([], legit)
        else:
            try:
                data = resp.json()['response']['route'][0]['summary']
            except:
                legit = (0, "error in parsing data")
                return ([], legit)
            mode = {'type': 'scooter'}
        return ([Leg(self.origin, self.destination, mode, data['distance'], data['travelTime'])], legit)


if __name__ == '__main__':
    journey = Scooter((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary)