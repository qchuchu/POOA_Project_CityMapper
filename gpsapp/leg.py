class Leg:

    def __init__(self, origin, destination, mode=None, distance=None, duration=None, price=None):
        self.origin = origin
        self.destination = destination
        self.mode = {} if mode is None else mode
        self.distance = 0 if distance is None else distance
        self.duration = 0 if duration is None else duration
        self.price = 0 if price is None else price



