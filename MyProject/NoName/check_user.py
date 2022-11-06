import json
import os

directory = 'C:\\Users\\andre\\PycharmProjects\\book\\Part1 ' \
            '- Basics\\BookSection10 - Файлы и исключения\\file_directory\\refactor_username.json'


def get_stored_username():
    """Видобути збережене ім'я, якщо таке є"""
    filename = directory
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запитати ім'я користувача"""
    username = input("What is your name? ")
    with open(directory, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Привітати користувача на ім'я"""
    username = get_stored_username()
    if username is False:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        answer = input(f"Are you {username}. \nPrint 'Y' or 'N' if ye or no.\n ")
        if answer == 'Y':
            print(f"Welcome back, {username}!")
        if answer == 'N':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


# def check_name():
#     """Питає ім'я людей, якщо """

#  Проверка но пустое поле


greet_user()
