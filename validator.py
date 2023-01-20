from constants import CITY_MAPPER


class CityValidator:
    @staticmethod
    def validate(sensor_id, city):
        mapper = CITY_MAPPER[city]
        if sensor_id not in mapper.keys():
            raise ValueError("Sensor not in this city")

        return mapper[sensor_id]


class ValueValidator:
    @staticmethod
    def validate(value):
        if 0 < value < 1500:
            return value
        raise ValueError("Value not in range 0-1500")
