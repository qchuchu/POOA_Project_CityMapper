# This file contains the views of the function
from flask import Flask, request

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')


@app.route('/')
def index():
    return "Hello monde !"


@app.route('/itinerary', methods=['POST'])
def get_best_itinerary():
    # Get the user params and load the model
    pass


if __name__ == "__main__":
    print(app.config['APP_ID'])
    app.run()