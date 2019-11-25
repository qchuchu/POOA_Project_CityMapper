# GPSAPP - Centrale Mapper ![deer](deer.png)
*CentraleSupélec 2019 - Object-Oriented Programming Course*

*By Quentin Churet, Pauline Gloumeau & Thomas Descamps / September - December 2019*

Centrale Mapper is an app that enables you to look at the different modes of transport to go from an origin to a 
destination (in the region of Île-de-France, France only). The application can propose different modes of transport :
car, bike, walking, public transport, public bikes and public scooters.

On this repository, you can only find the backend part of the application. The front-end part is available here : 
[https://github.com/qchuchu/vue_gpsapp](https://github.com/qchuchu/vue_gpsapp).

The front-end server have been deployed on Netlify and the back-end on Heroku. The app is now available on :
[https://gpsapp-pooa.netlify.com/](https://gpsapp-pooa.netlify.com/).

## 1. Installation

### 1.1 API Server

1.1.1. Clone this repository

`git clone git@github.com:qchuchu/POOA_Project_CityMapper.git` with SSH

`git clone https://github.com/qchuchu/POOA_Project_CityMapper.git` with HTTPS

1.1.2 Install python

If you don't have python, please follow this url : 
[https://www.python.org/](https://www.python.org/)

1.1.3 Install pip

If you don't have pip, please follow this url : 
[https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

1.1.4 Install all dependencies

Move into the folder POOA_Project_CityMapper and run the following to install all the required dependencies :

`pip install -r requirements.txt`

1.1.5 Run API Server

Still in the folder, you need to export the following variables : 

Linux / MacOS: `export FLASK_APP=app`

Windows: `set FLASK_APP=app`

Then, you can run the API by typing `flask run`. The API will be available at http://127.0.0.1:5000/itineraries

The only method allowed is `POST`. Please see below to see how you can call the API.

## 1.2 Front-End Server

The Front-End Server installation process is available on the adapted Github : 
[https://github.com/qchuchu/vue_gpsapp](https://github.com/qchuchu/vue_gpsapp)

Once you have installed all the dependencies and launched the server, the front app will be available at the following
address : `localhost:8080`, and will directly call the API Server at http://127.0.0.1:5000/itineraries, by sending
`POST` requests.

# 2. Project's Description

## 2.1 How to call the API

Our API have only one endpoint, that only be accessed by sending `POST` requests, by sending a JSON. Here are
the parameters that you need to send to receive a response :

- origin : [latitude, longitude] or (latitude, longitude) where latitude and longitude are `type:float`.
- destination : [latitude, longitude] or (latitude, longitude) where latitude and longitude are `type:float`.
- 
