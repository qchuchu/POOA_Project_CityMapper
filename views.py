# This file contains the views of the function
from app import app
from flask import request
from json import loads
from flask_cors import CORS
from transportation_api.itinerary_optimizer import ItineraryOptimizer

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/itineraries', methods=['POST'])
def get_best_itinerary():
    data = request.get_json()
    if not data:
        data = loads(request.get_data().decode('utf-8'))
    try:
        optimizer = ItineraryOptimizer(data)
        optimizer.run()
        response_object = {'status': 'success', 'itineraries': optimizer.get_itineraries_json()}
    except AttributeError as e:
        response_object = {'status': 'failed', 'explanation': 'wrong argument'}
    return response_object
