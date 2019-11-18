class Itinerary:
    """
    Itinerary object that contains all the information about the itinerary given an origin and a destination
    """
    def __init__(self, origin, destination, legs=None, legit = None):
        self.origin = origin
        self.destination = destination
        self._legs = [] if legs is None else legs
        if legit is None:
            if legs is None:
                self._legit = (0, "legs empty")
            else:
                self._legit = (1, "legs unempty")
        else:
            self._legit = legit

    def add(self, value):
        # Check if value is Leg
        self._legs.append(value)

    @property
    def legit(self):
        return self._legit

    @property
    def legs(self):
        return self._legs

    def get_total_price(self):
        total_price = 0
        for i in self.legs:
            total_price += i.price
        return total_price

    def get_total_distance(self):
        total_distance = 0
        for i in self.legs:
            total_distance += i.distance
        return total_distance

    def get_total_duration(self):
        total_duration = 0
        for i in self.legs:
            total_duration += i.duration
        return total_duration

    def get_number_of_legs(self):
        return len(self.legs)

    def __add__(self, other):
        origin = self.origin
        destination = other.destination
        legs = self.legs + other.legs
        return Itinerary(origin, destination, legs)