import requests
from gpsapp.transportation import Transportation


class Bike(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('bicycle')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        self.itinerary.distances.append(data['distance'])
        self.itinerary.times.append(data['travelTime'])
        self.itinerary.modes.append('Bike')
        return self.itinerary


if __name__ == '__main__':
    trajet1 = Bike((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(trajet1.get_itinerary().distances)













