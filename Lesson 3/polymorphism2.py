class Car:
    def __init__(self, name):
        self._speed_name_map = {
            "BMV": 250,
            "MERCEDES": 350
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self._speed_name_map.get(name, 0)

    def distance_on_max_speed(self, distance):
        if self._max_speed == 0:
            print(
                "Speed = 0, select valid car brand: {}".format(
                    list(self._speed_name_map.keys())
                )
            )
            return 0
        return distance / self._max_speed

car1 = Car('BMV')
car2 = Car('MERCEDES')
car3 = Car('ABC')

print(car1.distance_on_max_speed(167))
print(car2.distance_on_max_speed(167))
print(car3.distance_on_max_speed(167))
