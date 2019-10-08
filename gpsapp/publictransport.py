import requests


class PublicTransport:
    """ Cette classe retournera un objet itinéraire qui donnera des informations sur un trajet en transports publics
    entre deux positions gps (essentiellement ratp)'"""

    def __init__(self, waypoint0, waypoint1):
        #Position GPS de départ
        self.waypoint0 = waypoint0
        #Position GPS d'arrivée
        self.waypoint1 = waypoint1

    def run(self):

        base = 'https://route.api.here.com/routing/7.2/calculateroute.json'
        # app_id = '?app_id=' + os.environ[APP_ID]
        # a
        app_id = '?app_id=djGZJjsUab93vV3VqBKA'
        app_code = '&app_code=u3bReKn8wIAuZl74j1iyGA'
        mode = "&departure=now&mode=fastest;publicTransport&combineChange=true"
        waypoint0 = '&waypoint0=geo!' + departure
        waypoint1 = '&waypoint1=geo!' + arrival
        final = base + app_id + app_code + waypoint0 + waypoint1 + mode

        url = base + '?app_id=' + app_id + '&app_code=' + app_code + "&waypoint0=geo!" + departure + "&waypoint1=geo!" + arrival + "&departure=now&mode=fastest;PublicTransport&combineChange=true"
        resp = requests.get(final)
        # resp = requests.get('https://transit.api.here.com/v3/route.json?dep=48.8747%2C2.2952&arr=48.8474%2C2.3932&time=2019-09-24T07%3A30%3A00&app_id=devportal-demo-20180625&app_code=9v2BkviRwi9Ot26kp2IysQ&routing=tt')
        # resp = requests.get('https://transit.api.here.com/v3/route.json', params={'dep': departure, 'arr': arrival, 'time': time, "app_id" : app_id, "app_code" : app_code, 'routing' : 'tt'})
        try:
            assert resp.status_code == 200
            print('Ceci est la réponse')
            print(resp.json())
        except AssertionError:
            print("API Call didn't work")



