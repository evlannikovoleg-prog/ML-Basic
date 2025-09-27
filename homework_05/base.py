"""
Доработайте класс `Vehicle`
"""
from homework_05.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=1000, started=False, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if self.started:
            print("Стартер сломаешь. Уже заведено.")
        else:
            if self.fuel > 0:
                print("Стартуем...")
                self.started = True
            else:
                #print("HE Стартуем...")
                raise LowFuelError()

            
    pass


if __name__ == "__main__":
    car = Vehicle(100, False, 0, 150)
    car.start()
