# 9-6 Візочок з морозивом
# from class_dog__restaurant_ex import Restaurant
#
#
# class IceCreamStand(Restaurant):
#     """
#     Змоделювати властивості для наповнювача морозива
#     """
#
#     def __init__(self, restaurant_name, cuisine_type='IceCream Shop'):
#         """
#             Започаткувати атрибути батьківського класу.
#             Тоді ініціалізувати атрибути наповнювача морозива.
#         """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
#
#     def show_flavors(self):
#         """Показує наповнювачі"""
#         print(f"\nWe have this flavors for your ice cream:")
#         for flavor in self.flavors:
#             print(f" - {flavor.title()}")
#
#
# big_ice = IceCreamStand('Big Ice Cream')
# big_ice.flavors = ['vanilla', 'chocolate', 'lemon']
#
# big_ice.describe_restaurant()
# big_ice.show_flavors()

# 9-7 Адмін

from class_dog__restaurant_ex import User


class Admin(User):
    """Властивості класу адмін"""

    def __init__(self, first_name, last_name, city, age):
        """Започаткувати атрибути батьківського класу."""
        super().__init__(first_name, last_name, city, age)
        self.privileges = Privileges()


# user_1 = Admin("Andrii", "Saienko", "Kiev", "21")
# user_1.describe_user()
#
# user_1.privileges = [
#     'can add post',
#     'can ban user',
#     'can delete post',
# ]
#
# user_1.show_privileges()

# 9-8 Переваги

class Privileges:
    """Для зберігання прав адміну(ПРИВІЛЕЙ)"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Показує переваги"""
        print(f"\nHello, Admin!"
              f"\nYou can do this:")
        for privilege in self.privileges:
            print(f" - {privilege.title()}")


# user_1 = Admin("Andrii", "Saienko", "Kiev", "21")
# user_1.describe_user()
# user_1.privileges.show_privileges()
#
# print("\nAdding privileges...")
#
# user_1_privileges = [
#     'can add post',
#     'can ban user',
#     'can delete post']
#
# user_1.privileges.privileges = user_1_privileges
# user_1.privileges.show_privileges()

# 9-9 Оновити батареї

from inheritance import ElectricCar, Battery

electric_car = ElectricCar('porsche', 'taycan', 2022)
electric_car.battery.get_range()

electric_car.battery.upgrade_battery()
electric_car.battery.get_range()
