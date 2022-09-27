# 9-4

class Restaurant:
    """Моделювання ресторану"""

    def __init__(self, restaurant_name, cuisine_type):
        """Ініціалізація атрибутів імені та типу кухні"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Виводить назву та тип кухні"""
        print(f"\nRestaurant name is: {self.restaurant_name}.")
        print(f"Type of this restaurant is: {self.cuisine_type}")

    def open_restaurant(self):
        """Виводить інформацію, чи відчинений ресторан"""
        print(f"{self.restaurant_name} now is opened!")

    def read_clients(self):
        """Вивести повідомлення з кількістю відвідувачів"""
        print(f"Amount of clients today: {self.number_served}")

    def set_number_served(self, count):
        """Задати значення клієнтів"""
        self.number_served = count

    def increment_number_served(self, clients):
        """Додати значення відвідувачів за день"""
        self.number_served += clients


# restaurant_1 = Restaurant('Aroma Kava', 'coffee')
# restaurant_1.describe_restaurant()
# # restaurant_1.number_served = 25
#
# restaurant_1.set_number_served(60)
# restaurant_1.read_clients()
#
# restaurant_1.increment_number_served(10)
# restaurant_1.read_clients()

# 9-5

class User:
    """Моделювання юзера"""

    def __init__(self, first_name, last_name, city, age, ):
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
        self.login_attempts = 0

    def describe_user(self):
        """Виводить інформацію про користувача"""
        print(f"\nUser name is {self.first_name}, last name of user is {self.last_name}. "
              f"User live in {self.city}, and user age is {self.age}")

    def greet_user(self):
        """Виводить привітання дол користувача"""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def read_login_tries(self):
        """"""
        print(f"All login tries count are: {self.login_attempts}")

    def increment_login_attempts(self):
        """"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """"""
        self.login_attempts = 0


first_user = User('Andrii', 'Saienko', 'Kyiv', 21)
second_user = User('Mykyta', 'Kovalskyi', 'Kyiv', 22)
third_user = User('Veronika', 'Pipnik', 'Kotsubinske', 19)

first_user.describe_user()
first_user.greet_user()
first_user.read_login_tries()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()

first_user.read_login_tries()
first_user.reset_login_attempts()
first_user.read_login_tries()

second_user.describe_user()
second_user.greet_user()
second_user.read_login_tries()
second_user.increment_login_attempts()
second_user.read_login_tries()

third_user.describe_user()
third_user.greet_user()
third_user.read_login_tries()
third_user.increment_login_attempts()
third_user.read_login_tries()
