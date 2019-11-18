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



"""
Add Multi Threading
"""



class ItineraryOptimizer:
    """
    This class will optimize the different API Calls
    """

    itineraries = []

    def __init__(self, _user_params):
#    def __init__(self, **user_params):

        #for key, value in user_params.items():
        #    setattr(self, key, value)
        self._user_params = _user_params
        self.transportation_mode = {'bike': 1, 'car': 1, 'pedestrian': 1, 'scooter': 1, 'publicbike': 1, 'publictransport': 1, 'publicscooter': 1}



    def _select_itineraries(self):
#This fonction selects only the itineraries that the user can take based on the parameters he entered

        self._weather()
        self._hasacar()
        self._hasascooter()
        self._hasabike()
        self._isalone()
        self._isloaded()
        self._hasdisabilities()
        return self.transportation_mode

    def _weather(self):
        """Update the transport mode"""
        w = Weather()
        gw = w.get_weather()
        sky_desc = gw[0]
        temperature = gw[2]
        windspeed = gw[3]
        if (sky_desc == 'sunny') or (sky_desc == 'clear') or (sky_desc == 'cloudy') or (sky_desc == 'hail'):
            self.transportation_mode = self.transportation_mode
        else :
            self.transportation_mode['bike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['pedestrian']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['publicbike']=0
            return(self.transportation_mode)

    def _isalone(self):
        if self._user_params['alone'] is False :
            self.transportation_mode['bike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['publicbike']=0

    def _hasacar(self):
        if ('car' in self._user_params['vehicles']) is False:
            self.transportation_mode['car']=0

    def _hasabike(self):
        if ('bike' in self._user_params['vehicles']) is False:
            self.transportation_mode['bike']=0

    def _hasascooter(self):
        if ('scooter' in self._user_params['vehicles']) is False:
            self.transportation_mode['scooter']=0

    def _isloaded(self):
        if self._user_params['loaded'] is True:
            self.transportation_mode['bike']=0
            self.transportation_mode['publicbike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0

    def _hasdisabilities(self):
        if self._user_params['disabled'] is True :
            self.transportation_mode['bike']=0
            self.transportation_mode['publicbike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['pedestrian']=0


    def _calculate_itineraries(self):

        transportation = self._select_itineraries()
        itineraries = []
# ajouter du multithreading
        if transportation['bike']==1:
            bike = Bike(self._user_params['origin'], self._user_params['destination'])
            #bike = Bike(self.origin, self.destination)
            if bike.itinerary.legit[0]==0:
                itineraries = itineraries + [bike.itinerary]

        if transportation['car'] == 1:
            car = Car(self._user_params['origin'], self._user_params['destination'])
            # car = Car(self.origin, self.destination)
            if car.itinerary.legit[0] == 0:
                itineraries = itineraries + [car.itinerary]

        if transportation['pedestrian'] == 1:
            pedestrian = Pedestrian(self._user_params['origin'], self._user_params['destination'])
            # pedestrian = Pedestrian(self.origin, self.destination)
            if pedestrian.itinerary.legit[0] == 0:
                itineraries = itineraries + [pedestrian.itinerary]

        if transportation['scooter'] == 1:
            scooter = Scooter(self._user_params['origin'], self._user_params['destination'])
            # scooter = Scooter(self.origin, self.destination)
            if scooter.itinerary.legit[0] == 0:
                itineraries = itineraries + [scooter.itinerary]

        if transportation['publicbike'] == 1:
            publicbike = PublicBike(self._user_params['origin'], self._user_params['destination'])
            # publicbike = PublicBike(self.origin, self.destination)
            if publicbike.itinerary.legit[0] == 0:
                itineraries = itineraries + [publicbike.itinerary]

        if transportation['publictransport'] == 1:
            publictransport = PublicTransport(self._user_params['origin'], self._user_params['destination'])
            # publictransport = PublicTransport(self.origin, self.destination)
            if publictransport.itinerary.legit[0] == 0:
                itineraries = itineraries + [publictransport.itinerary]

        if transportation['publicscooter'] == 1:
            publicscooter = PublicScooter(self._user_params['origin'], self._user_params['destination'])
            # publicscooter = PublicScooter(self.origin, self.destination)
            if publicscooter.itinerary.legit[0] == 0:
                itineraries = itineraries + [publicscooter.itinerary]


        return itineraries

def sort_itineraries(self):
    pass






io = ItineraryOptimizer({'origin': (48.8586, 2.284249999999929), 'destination': (48.725873, 2.262104), 'vehicles': ['car', 'scooter'], 'mode': 'fastest','alone': True, 'loaded': False, 'disabled': False})
print(io._select_itineraries())
print(io._calculate_itineraries())



