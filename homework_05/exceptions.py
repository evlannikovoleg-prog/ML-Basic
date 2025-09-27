"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Топлива нет в баке."

class NotEnoughFuel(Exception):
    def __init__(self, dest, fuel):
        self.dest = dest
        self.fuel = fuel
        pass
    def __str__(self):
        return f"Не доедем до пункта назначения {self.dest} с таким уровнем топлива: {self.fuel}."

class CargoOverload(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Перегруз."
