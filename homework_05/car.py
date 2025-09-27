"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    def __init__(self, type):
        if type == '4клоп':
            self.pistons = 4
            self.volume = 1600
        elif type == 'вэвосемь':
            self.pistons = 8
            self.volume = 8888
        self._engine = Engine(self.pistons, self.volume)
        super().__init__()

    def set_engine(self, engine: Engine):
        self._engine = engine
        print(engine)

if __name__ == "__main__":
    car = Car('4клоп')
    car.start()
    car.move(5)
