class Car:
    """Проста спроба змоделювати машину"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів, що описують машину"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Повернути відформатоване змістовне ім'я."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
