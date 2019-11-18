import requests
from weather import Weather
from bike import Bike
from car import Car
from itinerary import *
from pedestrian import Pedestrian
from publicbike import PublicBike
from publicscooter import PublicScooter
from publictransport import PublicTransport
from scooter import Scooter
from transportation import *
from leg import *
from views import *


class ItineraryOptimizer:
    """
    This class will optimize the different API Calls
    """

    def __init__(self, user_params):
        for key, value in user_params.items():
            setattr(self, "_" + key, value)
        self._itineraries = []
        self.transportation_mode = {'bike': 1, 'car': 1, 'pedestrian': 1, 'scooter': 1, 'public_bike': 1,
                                    'public_transport': 1, 'public_scooter': 1}

    def _select_itineraries(self):
        # This fonction selects only the self._itineraries that the user can take based on the parameters he entered
        #self._weather_filter()
        self._has_car()
        self._has_scooter()
        self._has_bike()
        self._is_alone()
        self._is_loaded()
        self._has_disabilities()

    def _weather_filter(self):
        """Take into account the weather. If it's raining or """
        weather = Weather()
        gw = weather.get_weather()
        sky_desc = gw[0]
        temperature = gw[2]
        windspeed = gw[3]
        if sky_desc not in ['sunny', 'clear', 'cloudy', 'hail']:
            self.transportation_mode['bike'] = 0
            self.transportation_mode['scooter'] = 0
            self.transportation_mode['pedestrian'] = 0
            self.transportation_mode['public_scooter'] = 0
            self.transportation_mode['public_bike'] = 0

    def _is_alone(self):
        if not self._alone:
            self.transportation_mode['bike'] = 0
            self.transportation_mode['scooter'] = 0
            self.transportation_mode['public_scooter'] = 0
            self.transportation_mode['public_bike'] = 0

    def _has_car(self):
        if 'car' not in self._vehicles:
            self.transportation_mode['car'] = 0

    def _has_bike(self):
        if 'bike' not in self._vehicles:
            self.transportation_mode['bike'] = 0

    def _has_scooter(self):
        if 'scooter' not in self._vehicles:
            self.transportation_mode['scooter'] = 0

    def _is_loaded(self):
        if self._loaded:
            self.transportation_mode['bike'] = 0
            self.transportation_mode['public_bike'] = 0
            self.transportation_mode['scooter'] = 0
            self.transportation_mode['public_scooter'] = 0

    def _has_disabilities(self):
        if self._disabled:
            self.transportation_mode['bike'] = 0
            self.transportation_mode['public_bike'] = 0
            self.transportation_mode['scooter'] = 0
            self.transportation_mode['public_scooter'] = 0
            self.transportation_mode['pedestrian'] = 0

    def _calculate_itineraries(self):

        # ajouter du multithreading
        if self.transportation_mode['bike'] == 1:
            bike = Bike(self._origin, self._destination)
            # bike = Bike(self.origin, self.destination)
            if bike.is_legit():
                self._itineraries = self._itineraries + [bike.itinerary]

        if self.transportation_mode['car'] == 1:
            car = Car(self._origin, self._destination)
            # car = Car(self.origin, self.destination)
            if car.is_legit():
                self._itineraries = self._itineraries + [car.itinerary]

        if self.transportation_mode['pedestrian'] == 1:
            pedestrian = Pedestrian(self._origin, self._destination)
            # pedestrian = Pedestrian(self.origin, self.destination)
            if pedestrian.is_legit():
                self._itineraries = self._itineraries + [pedestrian.itinerary]

        if self.transportation_mode['scooter'] == 1:
            scooter = Scooter(self._origin, self._destination)
            # scooter = Scooter(self.origin, self.destination)
            if scooter.is_legit():
                self._itineraries = self._itineraries + [scooter.itinerary]

        if self.transportation_mode['public_bike'] == 1:
            public_bike = PublicBike(self._origin, self._destination)
            # public_bike = public_bike(self.origin, self.destination)
            if public_bike.is_legit():
                self._itineraries = self._itineraries + [public_bike.itinerary]

        if self.transportation_mode['public_transport'] == 1:
            public_transport = PublicTransport(self._origin, self._destination)
            if public_transport.is_legit():
                self._itineraries = self._itineraries + [public_transport.itinerary]

        if self.transportation_mode['public_scooter'] == 1:
            public_scooter = PublicScooter(self._origin, self._destination)
            if public_scooter.is_legit():
                self._itineraries = self._itineraries + [public_scooter.itinerary]

    def _sort_itineraries(self):
        if self._mode == 'fastest':
            self._itineraries.sort(key=lambda x: x.get_total_duration())
        elif self._mode == 'cheapest':
            pass
        elif self._mode == 'less_steps':
            pass

    def run(self):
        self._select_itineraries()
        self._calculate_itineraries()
        self._sort_itineraries()


if __name__ == '__main__':
    io = ItineraryOptimizer(
        {'origin': (48.8586, 2.284249999999929), 'destination': (48.725873, 2.262104), 'vehicles': ['car', 'scooter'],
         'mode': 'fastest', 'alone': True, 'loaded': False, 'disabled': False})
    io.run()
    print(io._itineraries)
