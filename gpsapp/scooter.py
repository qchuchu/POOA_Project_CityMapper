from bike import Bike
from leg import Leg


class Scooter(Bike):

    def get_itinerary(self):
        super().get_itinerary()
        self.itinerary.modes = ['Scooter']
        return self.itinerary


if __name__ == '__main__':
    journey = Scooter((48.8586, 2.284249999999929), (48.725873, 2.262104))
    print(journey.itinerary)