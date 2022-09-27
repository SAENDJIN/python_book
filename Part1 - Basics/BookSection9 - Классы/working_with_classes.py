class Car:
    """Проста спроба змоделювати машину"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів, що описують машину"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10

    def get_descriptive_name(self):
        """Повернути відформатоване змістовне ім'я."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """Вивести повідомлення з пробігом автомобіля"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Задати значення одометру
        Відкинути змінну в разі спроби відмотати показник одометру.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer")

    def increment_odometer(self, miles):
        """Додати задане значення до показника одометра."""
        if miles < 0:
            print("You can't add a minus value")
        else:
            self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(223)
# my_new_car.read_odometer()

my_used_car = Car('subaru', 'impreza', 2007)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(350_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(0.1)
my_used_car.read_odometer()
