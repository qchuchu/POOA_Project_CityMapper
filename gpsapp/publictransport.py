import requests
from transportation import Transportation, get_request
from bs4 import BeautifulSoup
from leg import Leg


class PublicTransport(Transportation):

    dict_keys = {'station' : 'station', 'line' : 'line', 'departure_station' : 'station', 'arrival_station':'destination', 'number of stops':'stops', 'next street' : 'next-street'}

    def _get_itinerary(self):
        legs = []
        legit = (1, 'legit itinerary')
        url = self.url_here_routing_api('public')
        print(url)
        resp, stat = get_request(url)
        legs = []
        if stat != "successfull":
            legit = (0, stat)
            return([], legit)
        else:
            try:
                data = resp.json()['response']['route'][0]['leg'][0]['maneuver']
            except:
                legit = (0, "error in parsing data")
                return ([], legit)
            for i in data:
                try:
                    position = i["position"]
                    origin = (position["latitude"], position['longitude'])
                    duration = i["travelTime"]
                    distance = i["length"]
                    mode = {}
                    soup = BeautifulSoup(i['instruction'], "html.parser")
                    try:
                        transport_mode = soup.find_all('span', attrs={"class" : u"transit"})[0].string
                    except:
                        transport_mode = "pedestrian"
                    mode['transport_mode'] = transport_mode
                    for l in self.dict_keys.keys():
                        try:
                            mode[l] = soup.find_all('span', attrs={"class" : self.dict_keys[l]})[0].string
                        except:
                            pass
                    legs.append(Leg(origin, origin, mode, distance, duration, None))
                except:
                    pass
            return (legs,legit)


if __name__ == '__main__':
    journey = PublicTransport((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary.legs)