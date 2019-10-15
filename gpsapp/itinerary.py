class Itinerary:
    """
    Itinerary object that contains all the information about the itinerary given an origin and a destination
    """
    def __init__(self, origin, destination, legs=None):
        self.origin = origin
        self.destination = destination
        self._legs = [] if legs is None else legs

    def add(self, value):
        # Check if value is Leg
        self._legs.append(value)

    def get_total_price(self):
        pass

    def get_total_distance(self):
        pass

    def get_total_duration(self):
        pass

    def __add__(self, other):
        origin = self.origin
        destination = other.destination
        legs = self.legs + other.legs
        return Itinerary(origin, destination, legs)

