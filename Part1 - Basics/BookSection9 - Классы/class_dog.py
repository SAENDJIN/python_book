# 3 принципи ООП - Спадковість / Поліморфізм / Інкапсуляція
class Dog:  # Клас Dog це набір інструкцій, що вказує як робити індивідуальні екземпляри.
    # Класи ми називаємо з великої літери!
    """Проста спроба змоделювати собаку"""

    def __init__(self, name, age):  # Це метод init. Усі функції в класі є методами
        # Self - це обов'язковий параметр для визначення методу.
        """Ініціювати атрибути ім'я та вік."""
        self.name = name  # Будь-яка змінна якій ми надаємо префікс self, доступна до кожного методу в класі.
        # //Екземпляр = класс в якому є свої атрибути, тобто ми надаємо name та age конкретній собаці
        self.age = age  # Змінні доступні у всіх екземплярах називаються атрибутами.

    def sit(self):
        """Симулювати виконання команди 'сидіти'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Симулювати виконання команди 'лежати'."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
