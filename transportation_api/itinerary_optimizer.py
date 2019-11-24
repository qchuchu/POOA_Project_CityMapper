from transportation_api.weather import Weather
from transportation_api.bike import Bike
from transportation_api.car import Car
from transportation_api.pedestrian import Pedestrian
from transportation_api.public_bike import PublicBike
from transportation_api.public_scooter import PublicScooter
from transportation_api.public_transport import PublicTransport
from transportation_api.scooter import Scooter
import threading


class ItineraryOptimizer:
    """
    This class will optimize the different API Calls, and return a dictionnary containing the different informations
    """

    def __init__(self, user_params):
        for key, value in user_params.items():
            setattr(self, "_" + key, value)
        self._itineraries = []
        self.transportation_mode = {'bike': 1, 'car': 1, 'pedestrian': 1, 'scooter': 1, 'public_bike': 1,
                                    'public_transport': 1, 'public_scooter': 1}
        self.lock = threading.Lock()

    @property
    def itineraries(self):
        return self._itineraries

    def _weather_filter(self):
        """Take into account the weather. If it's raining or """
        weather = Weather()
        gw = weather.get_weather()
        sky_desc = gw[0]
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
        elif 'bike' in self._vehicles:
            self.transportation_mode['public_bike'] = 0

    def _has_scooter(self):
        if 'scooter' not in self._vehicles:
            self.transportation_mode['scooter'] = 0
        elif 'scooter' in self._vehicles:
            self.transportation_mode['public_scooter'] = 0

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

    def bike_itinerary(self):
        if self.transportation_mode['bike'] == 1:
            bike = Bike(self._origin, self._destination)
            # bike = Bike(self.origin, self.destination)
            if bike.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [bike.itinerary]
                self.lock.release()

    def car_itinerary(self):
        if self.transportation_mode['car'] == 1:
            car = Car(self._origin, self._destination)
            # car = Car(self.origin, self.destination)
            if car.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [car.itinerary]
                self.lock.release()

    def pedestrian_itinerary(self):
        if self.transportation_mode['pedestrian'] == 1:
            pedestrian = Pedestrian(self._origin, self._destination)
            if pedestrian.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [pedestrian.itinerary]
                self.lock.release()

    def scooter_itinerary(self):
        if self.transportation_mode['scooter'] == 1:
            scooter = Scooter(self._origin, self._destination)
            if scooter.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [scooter.itinerary]
                self.lock.release()

    def public_bike_itinerary(self):
        if self.transportation_mode['public_bike'] == 1:
            public_bike = PublicBike(self._origin, self._destination)
            if public_bike.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [public_bike.itinerary]
                self.lock.release()

    def public_transportation_itinerary(self):
        if self.transportation_mode['public_transport'] == 1:
            public_transport = PublicTransport(self._origin, self._destination)
            if public_transport.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [public_transport.itinerary]
                self.lock.release()

    def public_scooter_itinerary(self):
        if self.transportation_mode['public_scooter'] == 1:
            public_scooter = PublicScooter(self._origin, self._destination)
            if public_scooter.is_legit():
                self.lock.acquire()
                self._itineraries = self._itineraries + [public_scooter.itinerary]
                self.lock.release()

    def _select_itineraries(self):
        self._weather_filter()
        self._has_car()
        self._has_scooter()
        self._has_bike()
        self._is_alone()
        self._is_loaded()
        self._has_disabilities()

    def _calculate_itineraries(self):
        threading_bike = threading.Thread(target=self.bike_itinerary)
        threading_car = threading.Thread(target=self.car_itinerary)
        threading_pedestrian = threading.Thread(target=self.pedestrian_itinerary)
        threading_scooter = threading.Thread(target=self.scooter_itinerary)
        threading_public_bike = threading.Thread(target=self.public_bike_itinerary)
        threading_public_transportation = threading.Thread(target=self.public_transportation_itinerary)
        threading_public_scooter = threading.Thread(target=self.public_scooter_itinerary)
        list_threading = [threading_bike, threading_car, threading_pedestrian, threading_scooter, threading_public_bike,
                          threading_public_transportation, threading_public_scooter]
        for thread in list_threading:
            thread.start()
        for thread in list_threading:
            thread.join()
        pass

    def _sort_itineraries(self):

        if self._mode == 'fastest':
            self.itineraries.sort(key=lambda x: x.get_total_duration())
        elif self._mode == 'cheapest':
            self.itineraries.sort(key=lambda x: x.get_total_price())
        elif self._mode == 'less_steps':
            self.itineraries.sort(key=lambda x: x.get_number_of_legs())
        elif self._mode == 'shortest':
            self.itineraries.sort(key=lambda x: x.get_total_distance())

    def _convert_all_origin_destination(self):
        for itinerary in self.itineraries:
            for leg in itinerary.legs:
                leg.convert_origin_destination()

    def get_itineraries_json(self):
        final_itineraries = []
        for index, itinerary in enumerate(self.itineraries):
            itinerary_json = itinerary.get_itinerary_json()
            final_itineraries.append(itinerary_json)
        return final_itineraries

    def run(self):
        self._select_itineraries()
        self._calculate_itineraries()
        self._sort_itineraries()
        self._convert_all_origin_destination()



