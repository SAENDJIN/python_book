from working_with_classes import Car


class ElectricCar(Car):
    """Змоделювати властивості, притаманні електрокарам"""

    def __init__(self, make, model, year):
        """
        Започаткувати атрибути батьківського класу.
        Тоді ініціалізувати атрибути електрокара.
        """
        super().__init__(make, model, year)  # Функція super дозволяє викликати метод батьківського класу
        self.battery_size = 75

    def describe_buttery(self):
        """Вивести повідомлення про розмір акумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Електрокари не мають бензобак!"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'models s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.describe_buttery()
