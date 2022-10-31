# 10-6 - Додавання
# print("Enter 'q' to quit")
# print("Give me two numbers, and I'll sum them:")
#
# while True:
#     first_number = input()
#     if first_number == 'q':
#         break
#     second_number = input()
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("You can't sum words (string)")
#     else:
#         print(answer)


# 10-7 - Калькулятор додавання - same as 10-6

# 10-8 - Коти та собаки

# def read_names(filename):
#     """Вивести на екран клички тварин"""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#         print(f"Sorry, I can't find {filename} to open it")
#
#
# dogs = 'file_directory/dogs.txt'
# cats = 'file_directory/cats.txt'
# filenames = [cats, dogs]
#
# for filename in filenames:
#     read_names(filename)

# 10-9 - Тихі коти та собаки

# def read_names_shy(filename):
#     """Вивести на екран клички тварин"""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#         pass
#
#
# dogs = 'file_directory/doasdags.txt'
# cats = 'file_directory/cats.txt'
# filenames = [cats, dogs]
#
# for filename in filenames:
#     read_names_shy(filename)

# 10-10 - Поширені слова

def count_words(filename):
    """Порахувати кількість слів у файлі"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename} to open it")
    else:
        word = 'pussy'
        words = content.lower().count(word)
        print(f"The file {filename} has about {words} words '{word}'")


filename = 'file_directory/Moby-Dick.txt'
count_words(filename)
