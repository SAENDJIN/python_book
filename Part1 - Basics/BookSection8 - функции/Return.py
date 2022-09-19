def get_formatted_name(first_name, last_name):
    """"Повернути відформатоване повне ім'я."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# ------------------------------

def get_formatted_name(first_name, last_name, middle_name=''):  # Не совсем понимаю как это работает
    """"Повернути відформатоване повне ім'я."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# ------------------------------

def build_person(first_name, last_name, age=None):
    """Повернути словник з інформацією про людину."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person["age"] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# ------------------------------

def get_formatted_name(first_name, last_name):
    """"Повернути відформатоване повне ім'я."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print('enter"q" at any time to quit.')
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Second name: ")
    if l_name == 'q':
        break

    formtted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formtted_name}")
