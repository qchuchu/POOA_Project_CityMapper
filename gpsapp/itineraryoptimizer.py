"""
Add Multi Threading
"""


class ItineraryOptimizer:
    """
    This class will optimize the different API Calls
    """

    def __init__(self, **user_params):
        for key, value in user_params.items():
            setattr(self, key, value)
        self._calculate_best_itineraries()

    def _calculate_best_itineraries(self):
        pass

