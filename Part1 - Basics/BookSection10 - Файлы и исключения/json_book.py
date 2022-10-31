# import json
#
# numbers = [2, 3, 4, 5, 7, 11, 13]
#
# filename = 'file_directory/numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)
#
# # ------------------------------
#
# with open(filename) as f:
#     numbers_read = json.load(f)
#
# print(numbers_read)

# ------------------------------

# import json
#
# username = input("What is your name? ")
# filename = 'file_directory/username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember yo when you comeback, {username}")
#
# with open(filename) as f_r:
#     username_read = json.load(f_r)
#     print(f"Welcome back, {username_read}!")
#
# ------------------------------

# import json
#
# """Завантажити ім'я користувача, якщо воно було вже збережене
#     В іншому разі запитати ім'я користувача та збережіть його."""
# filename = 'file_directory/username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember yo when you comeback, {username}")
# else:
#     print(f"Welcome back, {username}")