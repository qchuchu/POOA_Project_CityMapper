class Itinerary:

    def __init__(self,departure,arrival, mode, distance, time, price, steps):
        self.departure = departure
        self.arrival = arrival
        self._mode = mode
        self._distance = distance
        self._time = time
        self._price = price
        self._steps = steps

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

    def __str__(self):
        pass


    def __add__(self, other):
        return Itinerary(self.distance + other.distance, self.time + other.time, self.price + other.price, self.steps + other.steps)

