# 9-1 + 9-2
class Restaurant:
    """Моделювання ресторану"""

    def __init__(self, restaurant_name, cuisine_type):
        """Ініціалізація атрибутів імені та типу кухні"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Виводить назву та тип кухні"""
        print(f"\nRestaurant name is: {self.restaurant_name}.")
        print(f"Type of this restaurant is: {self.cuisine_type}")

    def open_restaurant(self):
        """Виводить інформацію, чи відчинений ресторан"""
        print(f"{self.restaurant_name} now is opened!")


burger_restaurant = Restaurant("McDonald's", "burger's")
sandwich_restaurant = Restaurant("Subways", "sandwich")
sushi_restaurant = Restaurant("Ninja sushi", "sushi")


# print(burger_restaurant.restaurant_name)
# print(burger_restaurant.cuisine_type)
#
# burger_restaurant.describe_restaurant()
# burger_restaurant.open_restaurant()
#
# burger_restaurant.describe_restaurant()
# sandwich_restaurant.describe_restaurant()
# sushi_restaurant.describe_restaurant()


class User:
    """Моделювання юзера"""

    def __init__(self, first_name, last_name, city, age):
        """
        Ініціалізація параметрів
        :param first_name: Ім'я
        :param last_name: Фамілія
        :param city: Місто
        :param age: Вік
        """
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        """Виводить інформацію про користувача"""
        print(f"\nUser name is {self.first_name}, last name of user is {self.last_name}. "
              f"User live in {self.city}, and user age is {self.age}")

    def greet_user(self):
        """Виводить привітання дол користувача"""
        print(f"Hello, {self.first_name} {self.last_name}!")


first_user = User('Andrii', 'Saienko', 'Kyiv', 21)
second_user = User('Mykyta', 'Kovalskyi', 'Kyiv', 22)
third_user = User('Veronika', 'Pipnik', 'Kotsubinske', 19)

# first_user.describe_user()
# first_user.greet_user()
#
# second_user.describe_user()
# second_user.greet_user()
#
# third_user.describe_user()
# third_user.greet_user()