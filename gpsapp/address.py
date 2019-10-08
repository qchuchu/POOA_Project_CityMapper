import requests
import json
import os

url = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?prox=41.8842%2C-87.6388%2C250&mode=retrieveAddresses&maxresults=1&gen=9&app_id=devportal-demo-20180625&app_code=9v2BkviRwi9Ot26kp2IysQ'
resp = requests.get(url)
data = resp.json()

