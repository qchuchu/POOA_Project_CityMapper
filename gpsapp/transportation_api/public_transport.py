import requests
from transportation_api.transportation import Transportation, get_request
from bs4 import BeautifulSoup
from transportation_api.leg import Leg


class PublicTransport(Transportation):

    dict_keys = {'departure_station': 'station',
                 'line_of_transit': 'line',
                 'direction': 'destination',
                 'number of stops': 'stops',
                 'street': 'next-street',
                 'walk during':'length'}

    def request_data(self):
        url = self.url_here_routing_api('public')
        response, status = get_request(url)
        if status == "successful":
            legit = (1, 'legit itinerary')
        else:
            legit = (0, status)
        return response, legit

    def extract_legs_from_data(self, data):
        legs, legit = [], (1, 'legit')
        for step in data:
            try:
                position = step["position"]
                origin = (position["latitude"], position['longitude'])
                destination = (position["latitude"], position['longitude'])
                duration = step["travelTime"]
                distance = step["length"]
                price = 1.9
                mode = {}
                soup = BeautifulSoup(step['instruction'], "html.parser")
            except KeyError:
                legit = (0, "leg couldn't be extracted")
                return [], legit

            try:
                transport_mode = soup.find_all('span', attrs={"class": u"transit"})[0].string
            except (KeyError, AttributeError, IndexError):
                transport_mode = "pedestrian"
            mode['transport_mode'] = transport_mode

            for l in self.dict_keys.keys():
                try:
                    mode[l] = soup.find_all('span', attrs={"class": self.dict_keys[l]})[0].string
                except (KeyError, AttributeError, IndexError):
                    pass
            legs.append(Leg(origin, origin, mode, distance, duration, price))
        return "publicTransport", legs, legit

    def _get_itinerary(self):
        response, legit = self.request_data()
        if legit[0] == 0:
            return [], legit[1]
        try:
            data = response.json()['response']['route'][0]['leg'][0]['maneuver']
        except KeyError:
            # Except there is a key error
            legit = (0, "error in parsing data")
            return [], legit[1]
        return self.extract_legs_from_data(data)


if __name__ == '__main__':
    journey = PublicTransport((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary.get_itinerary_json())
