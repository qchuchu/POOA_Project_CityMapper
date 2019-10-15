import requests

from gpsapp.transportation import Transportation


class Pedestrian(Transportation):

    def get_itinerary(self):
        url = self.url_here_routing_api('pedestrian')
        resp = requests.get(url)
        data = resp.json()['response']['route'][0]['summary']
        self.itinerary.distances.append(data['distance'])
        self.itinerary.times.append(data['travelTime'])
        self.itinerary.modes.append('Pedestrian')
        return self.itinerary


if __name__ == '__main__':
    print('********TRAJET A PIED**********')
    journey = Pedestrian((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.get_itinerary())
