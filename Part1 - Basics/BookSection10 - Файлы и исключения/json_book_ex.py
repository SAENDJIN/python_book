import json


# 10-11 - Улюблене число
# fav_num = []
#
#
# def ask_fav_num():
#     fav_num = input("Hi! Tell me your favourite number: ")
#     filename = 'file_directory/fav_num_ex'
#     with open(filename, 'w') as f:
#         json.dump(fav_num, f)
#
#
# def tell_fav_number_to_user():
#     filename = 'file_directory/fav_num_ex'
#     with open(filename) as f:
#         number = json.load(f)
#         print(f"I know that your favourite number is {number}")
#
#
# ask_fav_num()
# tell_fav_number_to_user()

# 10-12 - Згадати улюблене число

# try:
#     with open('file_directory/fav_num_ex.json') as f:
#         fav_num = json.load(f)
# except FileNotFoundError:
#     fav_num = input("Hi! Tell me your favourite number: ")
#     with open('file_directory/fav_num_ex.json', 'w') as f:
#         json.dump(fav_num , f)
# else:
#     print(f"I know that your favourite number is {fav_num}")


# 10-13 - Перевірка користувача

def get_stored_username():
    """Видобути збережене ім'я, якщо таке є"""
    filename = 'file_directory/username.json'
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
    filename = 'file_directory/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Привітати користувача на ім'я"""
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

#
# def check_username():
#     username = get_stored_username()
#     if username:
#         answer_name = input(f"Hi, are you {username}? \nPrint 'Y' if it is you or 'N' if no: ")
#         if answer_name == 'Y':
#             greet_user()
#         else:
#             get_new_username()
#             print(f"We'll remember you when you comeback, {username}")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you comeback, {username}")


greet_user()

#
# except json.de
# try:coder.JSONDecodeError