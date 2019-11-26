from transportation_api.transportation import Transportation, get_request
from bs4 import BeautifulSoup
from transportation_api.leg import Leg


def html_parser_class_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find_all('span')
    parser = {}
    for span in spans:
        parser[span.attrs['class'][0]] = span.text
    return parser


def start_pedestrian_part(step, pedestrian_part, position):
    if pedestrian_part['status']:
        pedestrian_part['destination'] = position
        pedestrian_part['distance'] += step['length']
        pedestrian_part['duration'] += step['travelTime']
    else:
        pedestrian_part['origin'] = position
        pedestrian_part['distance'] = step['length']
        pedestrian_part['duration'] = step['travelTime']
        pedestrian_part['status'] = True


def end_pedestrian_part(legs, pedestrian_part, position):
    if pedestrian_part['status']:
        pedestrian_part['destination'] = position
        walking_leg = Leg(pedestrian_part['origin'], pedestrian_part['destination'],
                          mode={'transport_mode': 'pedestrian'},
                          distance=pedestrian_part['distance'],
                          duration=pedestrian_part['duration'], price=0)
        legs.append(walking_leg)
    pedestrian_part['status'] = False


def start_transport_part(step_info, step, transport_part, position):
    transport_part['status'] = True
    transport_part['origin'] = position
    transport_part['origin_station'] = step['stopName']
    transport_part['distance'] = step['length']
    transport_part['duration'] = step['travelTime']
    for attribute in ['transit', 'line', 'stops']:
        if attribute in step_info:
            transport_part[attribute] = step_info[attribute]
    if 'destination' in step_info:
        transport_part['transport_destination'] = step_info['destination']


def end_transport_part(legs, step, transport_part, position):
    transport_part['destination'] = position
    transport_part['destination_station'] = step['stopName']
    if transport_part['transit'] == 'rail' and transport_part['line'][0] == 'T':
        transport_part['transit'] = 'tram'
    if transport_part['transit'] == 'train' and transport_part['line'][0] not in ['A', 'B', 'C', 'D', 'E']:
        transport_part['transit'] = 'transilien'
    transport_leg = Leg(transport_part['origin'], transport_part['destination'],
                        mode={'transport_mode': transport_part['transit'],
                              'line': transport_part['line'],
                              'transport_destination': transport_part['transport_destination'],
                              'stops': transport_part['stops'],
                              'origin_station': transport_part['origin_station'],
                              'destination_station': transport_part['destination_station']},
                        distance=transport_part['distance'],
                        duration=transport_part['duration'])
    legs.append(transport_leg)


class PublicTransport(Transportation):

    def request_data(self):
        url = self.url_here_routing_api('public')
        response, status = get_request(url)
        if status == "successful":
            legit = (1, 'legit itinerary')
        else:
            legit = (0, status)
        return response, legit

    def _extract_legs_from_data(self, step_list):
        legs, legit = [], (1, 'legit')
        pedestrian_part = {'status': False, 'origin': None, 'destination': None, 'distance': 0,
                           'duration': 0}
        transport_part = {'status': False, 'origin': None, 'destination': None, 'distance': 0,
                          'duration': 0, 'line': None, 'stops': None, 'transit': None, 'origin_station': None,
                          'destination_station': None, 'transport_destination': None}
        legs = []
        position = []
        for step in step_list:
            position = [step['position']['latitude'], step['position']['longitude']]
            if step['_type'] == 'PrivateTransportManeuverType':
                start_pedestrian_part(step, pedestrian_part, position)
            else:
                end_pedestrian_part(legs, pedestrian_part, position)
                step_info = html_parser_class_text(step['instruction'])
                if transport_part['status']:
                    end_transport_part(legs, step, transport_part, position)
                    if 'transit' in step_info:
                        start_transport_part(step_info, step, transport_part, position)
                    else:
                        transport_part['status'] = False
                else:
                    start_transport_part(step_info, step, transport_part, position)
        end_pedestrian_part(legs, pedestrian_part, position)
        return "publicTransport", legs, legit

    def _get_itinerary(self):
        response, legit = self.request_data()
        if legit[0] == 0:
            return [], legit
        try:
            data = response.json()['response']['route'][0]['leg'][0]['maneuver']
        except KeyError:
            # Except there is a key error
            legit = (0, "error in parsing data")
            return [], legit
        return self._extract_legs_from_data(data)
