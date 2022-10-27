# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

# ------------------------------

# print("Give me two numbers, and I'll divide them:")
# print("Enter 'q' to quit")
#
# while True:
#     first_number = input()
#     if first_number == 'q':
#         break
#     second_number = input()
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0")
#     else:
#         print(answer)

# ------------------------------

# filename = 'file_directory/Alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         content = f.read()
# except FileNotFoundError:
#     print(f"Sorry, I can't find {filename} to open it")
# else:
#     # Рахує приблизну кількість слів у файлі
#     words = content.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words")


# ------------------------------

def count_words(filename):
    """Порахувати кількість слів у файлі"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename} to open it")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")


filenames = ['file_directory/Alice.txt', 'file_directory/LittleWomen.txt', 'file_directory/Moby-Dick.txt',
             'file_directory/Siddhartha.txt']
for filename in filenames:
    count_words(filename)
