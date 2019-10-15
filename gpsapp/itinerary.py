class Itinerary:
    """
    Itinerary object that contains all the information about the itinerary given an origin and a destination
    """
    def __init__(self, origin, destination, steps=None, modes=None, distances=None, times=None, prices=None):
        self.origin = origin
        self.destination = destination
        self._steps = [] if steps is None else steps
        self._modes = [] if modes is None else modes
        self._distances = [] if distances is None else distances
        self._times = [] if times is None else times
        self._prices = [] if prices is None else prices

    @property
    def distances(self):
        return self._distances

    @property
    def times(self):
        return self._times

    @property
    def prices(self):
        return self._prices

    @property
    def steps(self):
        return self._steps

    @property
    def modes(self):
        return self._modes

    @modes.setter
    def modes(self, value):
        self._modes = value

    def __add__(self, other):
        origin = self.origin
        destination = other.destination
        total_steps = self.steps + [other.origin] + other.steps
        total_modes = self.modes + other.modes
        total_distances = self.distances + other.distances
        total_times = self.times + other.times
        total_prices = self.prices + other.prices
        return Itinerary(origin, destination, total_steps, total_modes, total_distances, total_times, total_prices)

