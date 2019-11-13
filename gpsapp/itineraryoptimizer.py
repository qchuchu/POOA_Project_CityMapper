import requests 
from weather import Weather


"""
Add Multi Threading
"""


class ItineraryOptimizer:
    """
    This class will optimize the different API Calls
    """

    itineraries = []

    def __init__(self, **user_params):
        for key, value in user_params.items():
            setattr(self, key, value)
        self._calculate_best_itineraries()
        self.transportation_mode = {'bike': 1, 'car': 1, 'pedestrian': 1, 'scooter': 1, 'publicbike': 1, 'publictransport': 1, 'publicscooter': 1}

#on va dire que le user param qui correspond au choix de tri de l'itineraire est un attribut qui s'appelle criteria
#et qui prend pour valeur un string 'fastest', 'shortest', 'less_steps'

#les users param qui correspondent aux coordonnees de depart et d'arrivee sont respectivement origin et destination




    def _select_itineraries(self):
#This fonction selects only the itinerary that the user can take based on the parameters he entered

        self._isalone()
        self._hasacar()
        self._hasabike()
        self._hasascooter()
        self._isloaded()
        self._hasdisabilities()

    def _weather(self):
        """Update the transport mode"""
        w = Weather()
        gw = w.get_weather()
        sky_desc = gw[0]
        temperature = gw[2]
        windspeed = gw[3]
        if (sky_desc == 'sunny') or (sky_desc == 'clear') or (sky_desc == 'cloudy') or (sky_desc = 'hail'):
            return(self.transportation_mode)
        else :
            self.transportation_mode['bike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['pedestrian']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['publicbike']=0
            return(self.transportation_mode)

    def _isalone(self):
        if self.alone is False :
            self.transportation_mode['bike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['publicbike']=0

    def _hasacar(self):
        if self.car is False :
            self.transportation_mode['car']=0

    def _hasabike(self):
        if self.bike is False :
            self.transportation_mode['bike']=0

    def _hasascooter(self):
        if self.scooter is False :
            self.transportation_mode['scooter']=0

    def _isloaded(self):
        if self.loaded is True :
            self.transportation_mode['bike']=0
            self.transportation_mode['publicbike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0

    def _hasdisabilities(self):
        if self.disabilities is True :
            self.transportation_mode['bike']=0
            self.transportation_mode['publicbike']=0
            self.transportation_mode['scooter']=0
            self.transportation_mode['publicscooter']=0
            self.transportation_mode['pedestrian']=0


    def calculate_itinerary(self):

        if self.transportation_mode['bike']==1:
            bike0 = Bike(self, origin, destination)
            itineraries = itineraries + [bike0.get_itinerary()]
        if self.transportation_mode['car']==1:
            itineraries = itineraries + [Car()]
        if self.transportation_mode['pedestrian']==1:
            itineraries = itineraries + [Pedestrian()]
        if self.transportation_mode['scooter'] == 1:
            itineraries = itineraries + [Scooter()]
        if self.transportation_mode['publicbike'] == 1:
            itineraries = itineraries + [PublicBike()]
        if self.transportation_mode['publictransport'] == 1:
            itineraries = itineraries + [PublicTransport()]
        if self.transportation_mode['publicscooter']==1:
            itineraries = itineraries + [PublicScooter()]

        return itineraries

    def order_itinerary(self):
        if self.criteria == "Shortest":

        elif self.criteria == "Fastest":

        elif self.criteria == "Less_Steps":





iti = ItineraryOptimizer()
iti._weather()


