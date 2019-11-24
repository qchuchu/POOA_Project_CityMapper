# This file contains the views of the function
from app import app
from flask import request
from flask_cors import CORS
from transportation_api.itinerary_optimizer import ItineraryOptimizer

ITINERARIES = []

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/itineraries', methods=['GET', 'POST'])
def get_best_itinerary():
    global ITINERARIES
    response_object = {'status': 'success'}
    if request.method == 'POST':
        del ITINERARIES[:]
        data = request.get_json()
        optimizer = ItineraryOptimizer(data)
        optimizer.run()
        response_object['itineraries'] = optimizer.get_itineraries_json()
        ITINERARIES = response_object['itineraries']
    elif request.method == 'GET':
        response_object['itineraries'] = ITINERARIES
    return response_object
