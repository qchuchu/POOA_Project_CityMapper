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






