"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, max_cargo):
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__()

    def load_cargo(self, cargo):
        new_cargo = self.cargo + cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload()

    def remove_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo

