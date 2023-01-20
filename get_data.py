"""
A module for interacting with the AirTube website.
"""

import requests

from constants import API_BASE_URL, USER_AGENT
from validator import CityValidator, ValueValidator


def get_sensors_data(city, url=API_BASE_URL, headers=USER_AGENT):
    """
       Gets the data from all sensors in the city.

        Args:
            city: for which city we want to get data

        Returns:
            A dict with key(the id of the sensor) and value(the data from the sensor)

        Example:
            {43552:
            {'location': 'ul. "Trayan Tanev"',
            'p10': 17.65,
            'p2.5': 8.13,
            'timestamp': '2023-01-20 07:14:05'}
    """
    data_from_request = []
    request = requests.get(url, headers)
    data_from_request.append(request.json())
    result = {}

    for sensor_data in data_from_request[0]:

        try:
            sensor_id = sensor_data['sensor']['id']
            p10 = ValueValidator.validate(float(sensor_data['sensordatavalues'][0]['value']))
            p25 = ValueValidator.validate(float(sensor_data['sensordatavalues'][1]['value']))
            timestamp = sensor_data['timestamp']
            location = CityValidator.validate(sensor_id, city)
            result.update({sensor_id: {'location': location, 'p10': p10, 'p2.5': p25, 'timestamp': timestamp}})
        except:
            ValueError('Missing info for this sensor id')
    return result
