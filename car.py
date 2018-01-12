# Работа с классами и экземплярами
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
        self.odometer_reading += miles

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(3200)
my_new_car.read_odometer()
