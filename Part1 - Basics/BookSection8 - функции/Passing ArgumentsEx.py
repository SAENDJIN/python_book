# 8-3

def make_shirt(size, text):
    """Выводит информацию про размер и принт футболки"""
    print(f"Size of your shirt is: {size.title()}")
    print(f"Print on your shirt is text: {text}")


make_shirt('s', 'Veronika')  # Позиційний аргумент
make_shirt(text='Andrii', size='m')  # Ключовий аргумент


# 8-4

def make_shirt(text, size='l'):
    """Выводит информацию про размер и принт футболки"""
    print(f"Size of your shirt is: {size.upper()}")
    print(f"Print on your shirt is text: {text}")


make_shirt('I love Python')
make_shirt('I love Python', size='m')
make_shirt('I hate Java', size='xl')


# 8-5

def describe_city(city, country='Ukraine'):
    """Выводит информацию про город и страну"""
    print(f"{city.title()} is in {country.title()}")


describe_city('Kiev')
describe_city('Washington', country='USA')
describe_city(city='Paris', country='France')
