# Метод __init__() класса-потомка
class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = self.make + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()

    def update_odometer(self, miles):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        odometer_new = self.odometer_reading + miles
        if odometer_new > self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("\nYou can't decrement odometer value!")

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)


my_tesla = ElectroCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
