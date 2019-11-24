# This file contains the views of the function
from app import app
from flask import request
from flask_cors import CORS
from transportation_api.itinerary_optimizer import ItineraryOptimizer

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/itineraries', methods=['POST'])
def get_best_itinerary():
    response_object = {'status': 'success'}
    data = request.get_json()
    optimizer = ItineraryOptimizer(data)
    optimizer.run()
    response_object['itineraries'] = optimizer.get_itineraries_json()
    return response_object
