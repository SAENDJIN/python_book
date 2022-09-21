import random

user_input = ''

number = random.randint(1, 99)
tryCounter = int(5)
# while tryCounter != (int(0)), user_input != (int(number)):

while user_input != (int(number)):
    try:
        user_input = int(input("Guess the number from 1 to 99\nUse only whole numbers:\n "))
    except ValueError:
        print("Sorry, I didn't understand that.\n")
        continue
    if user_input == int(number):
        print("Y guessed the number")
        break
    if user_input > int(99):
        tryCounter = tryCounter - 1
        print("Мудила ебаный не больше 99\n")
    if user_input < int(1):
        print("Мудила ебаный не меньше 1\n")
        tryCounter = tryCounter - 1
    if user_input < int(number) or tryCounter == 0:
        print("Try something bigger\n")
        tryCounter = tryCounter - 1
    else:
        print("Попытки кончились мудак")
    if user_input > int(number) or tryCounter == 0:
        print("Try something smaller")
        tryCounter = tryCounter - 1
    else:
        print("Попытки кончились мудак")
    if tryCounter == int(0):
        print("Попытки кончились мудак")
        break
