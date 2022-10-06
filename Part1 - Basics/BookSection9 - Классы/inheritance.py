from working_with_classes import Car


class ElectricCar(Car):
    """Змоделювати властивості, притаманні електрокарам"""

    def __init__(self, make, model, year):
        """
        Започаткувати атрибути батьківського класу.
        Тоді ініціалізувати атрибути електрокара.
        """
        super().__init__(make, model, year)  # Функція super дозволяє викликати метод батьківського класу
        self.battery = Battery()


class Battery:
    """Проста спроба змоделювати акумулятора електрокара"""

    def __init__(self, battery_size=75):
        """Ініціалізація атрибуту акумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вивести повідомлення про розмір акумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """
        Вивести повідомлення про відстань, яку може подолати авто
        відповідно до місткості акумулятора.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Оновлює значення батареї"""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Battery upgraded to 100kWh")
        else:
            print("The battery is already 100kWh or more.")


# my_tesla = ElectricCar('tesla', 'models s', 2019)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
