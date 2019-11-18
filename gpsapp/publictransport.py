import requests
from transportation import Transportation, get_request
from bs4 import BeautifulSoup
from leg import Leg


class PublicTransport(Transportation):

    dict_keys = {'station': 'station',
                 'line': 'line',
                 'departure_station': 'station',
                 'arrival_station': 'destination',
                 'number of stops': 'stops',
                 'next street': 'next-street'}

    def _get_itinerary(self):
        legs = []
        legit = (1, 'legit_itinerary')
        url = self.url_here_routing_api('public')
        response, status = get_request(url)
        legs = []
        # Check if we can contact the HERE API
        if status != "successful":
            legit = (0, status)
            return [], legit
        else:
            try:
                data = response.json()['response']['route'][0]['leg'][0]['maneuver']
            except:
                # Except there is a key error
                legit = (0, "error in parsing data")
                return [], legit
            # Modify i - It's not a clear variable. Use step
            for i in data:
                try:
                    position = i["position"]
                    origin = (position["latitude"], position['longitude'])
                    duration = i["travelTime"]
                    distance = i["length"]
                    mode = {}
                    soup = BeautifulSoup(i['instruction'], "html.parser")
                    try:
                        transport_mode = soup.find_all('span', attrs={"class": u"transit"})[0].string
                    except:
                        # Except the find_all don't work. Que fais string ?
                        transport_mode = "pedestrian"
                    mode['transport_mode'] = transport_mode
                    # Use key legInformation
                    for l in self.dict_keys.keys():
                        try:
                            mode[l] = soup.find_all('span', attrs={"class" : self.dict_keys[l]})[0].string
                        # Définir le type d'erreur
                        except:
                            pass
                    legs.append(Leg(origin, origin, mode, distance, duration, None))
                except:
                    pass
            return legs,legit


if __name__ == '__main__':
    journey = PublicTransport((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary.legs)