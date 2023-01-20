"""
    Gets data from AirTube and send notification for locations with high P10 and P2.5.
"""

from get_data import get_sensors_data
from telegram.telegram_m import send_msg
from validator import HighP10Validator, HighP25Validator


def get_high_values(city):
    """
    Check for high values and return a warning msg.

    Return:
        Message with information fow each location

    Example:
        Places in Sofia with high P10 and p2.5 values:
        - ul. "Kumata", P10: 3.7, P2.5: 99.8 measured on 13:15:17
        - ul. „Georgi S. Rakovski“, P10: 5.05, P2.5: 81.92 measured on 13:17:05
    """
    data_from_sensors = get_sensors_data(city)
    warning_msg = 'Places in Sofia with high P10 and p2.5 values:\n'
    for value in data_from_sensors.values():
        if HighP10Validator.validate(value['p10']) or HighP25Validator.validate(value['p2.5']):
            warning_msg += f'- {value["location"]}, P10: {value["p10"]},' \
                           f' P2.5: {value["p2.5"]} measured on {value["timestamp"][-8:]}\n'
    return warning_msg


def run(city):
    msg = get_high_values(city)
    send_msg(msg)


if __name__ == '__main__':
    run('Sofia')
