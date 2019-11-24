import requests

class Leg:

    def __init__(self, origin, destination, mode=None, distance=None, duration=None, price=None):
        self.origin = origin
        self.destination = destination
        self._mode = {} if mode is None else mode
        self._distance = 0 if distance is None else distance
        self._duration = 0 if duration is None else duration
        self._price = 0 if price is None else price

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        return self._duration

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_leg_json(self):
        leg_json = {'mode': self.mode, 'duration': self.duration, 'distance': self.distance, 'price': self.price,
                    'origin': self.origin, 'destination': self.destination}
        return leg_json

    def convert_origin_destination(self):
        base = "https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?"
        prox_origin = "prox={}%2C{}%2C250".format(self.origin[0], self.origin[1])
        prox_destination = "prox={}%2C{}%2C250".format(self.destination[0], self.destination[1])
        mode = "&mode=retrieveAddresses"
        maxresults = "&maxresults=1"
        gen = "&gen=9"
        app_id = '&app_id=yZ9PTsD28Zmv1i33vsKj'
        app_code = '&app_code=2w2uary6rOXjXAl9KyzsyA'
        path_origin = base + prox_origin + mode + maxresults + gen + app_id + app_code
        path_destination = base + prox_destination + mode + maxresults + gen + app_id + app_code
        origin_address = requests.get(path_origin)
        destination_address = requests.get(path_destination)
        try:
            self.origin = origin_address.json()['Response']['View'][0]['Result'][0]['Location']['Address']['Label']
            self.destination = destination_address.json()['Response']['View'][0]['Result'][0]['Location']['Address']['Label']
        except (IndexError, KeyError) as e:
            pass


if __name__ == '__main__':
    leg = Leg((48.8586, 2.284249999999929), (48.725873, 2.262104))
    leg.convert_origin_destination()
    print(leg.get_leg_json())





