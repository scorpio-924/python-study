
import car
my_car = car.Car("路虎", 80)
my_car.info()

from car import Car
my_car = Car("路虎",80)
my_car.info()

import car as c
my_car = c.Car("路虎",80)
my_car.info()

from car import *
my_car = Car("路虎",80)
my_car.info()