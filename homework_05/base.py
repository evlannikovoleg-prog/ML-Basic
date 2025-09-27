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
                # print("HE Стартуем...")
                raise LowFuelError()
    # метод move, который проверяет,
# что топлива достаточно для преодоления переданной дистанции
# (вплоть до полного расхода),
# и изменяет количество оставшегося топлива, иначе выкидывает
# исключение exceptions.NotEnoughFuel
    def move(self, distance):
        print(f"Топлива в баке: {self.fuel}л.")
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed > self.fuel:
            print("Маловато горючки.")
            raise NotEnoughFuel(distance, self.fuel)
        else:
            print(f"На маршрут {distance}км. при таком расходе ({self.fuel_consumption}л/км) уйдёт {fuel_needed}л. топлива... "
                  f"Многовато, конечно, но останется ещё {self.fuel - self.fuel_consumption}л.")

    pass


if __name__ == "__main__":
    car = Vehicle(100, False, 10, 150)
    car.start()
    car.move(5)
