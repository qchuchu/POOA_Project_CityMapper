class Itinerary:
    """
    Cette Classe est l'objet itinéraire que renverra chacune des classes de transport
        :

        :return:
    """
    def __init__(self, origin, destination, steps=[], modes=[], distances=[], times=[], prices=[]):
        self.origin = origin
        self.destination = destination
        self._steps = steps
        self._modes = modes
        self._distances = distances
        self._times = times
        self._prices = prices

    @property
    def distance(self):
        return self._distances

    @distance.setter
    def distance(self, value):
        self._value = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value

    def __add__(self, other):
        origin = self.origin
        destination = other.destination
        steps = self.steps + [other.origin] + other.steps
        modes = self.modes + other.modes
        distances = self.distances + other.distances
        times = self.times + other.times
        prices = self.prices + other.prices
        return Itinerary(origin, destination, steps, modes, distances, times, prices)

