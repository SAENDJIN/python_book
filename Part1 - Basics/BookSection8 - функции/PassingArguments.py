def describe_pet(animal_type, pet_name):
    """Показати інформацію про домашнього улюбленця"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# ------------------------------

def describe_pet(animal_type, pet_name):
    """Показати інформацію про домашнього улюбленця"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='dog', pet_name='willie')


# ------------------------------

def describe_pet(pet_name, animal_type='dog'):
    """Показати інформацію про домашнього улюбленця"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry', animal_type='humster')
describe_pet(pet_name='willie')

# Собака на ім'я Віллі
describe_pet('willie')
describe_pet(pet_name='willie')

# Хом'як на ім'я Гаррі
describe_pet('harry', 'hamster')


# ------------------------------

def describe_pet(pet_name, animal_type='dog'):
    """Показати інформацію про домашнього улюбленця (Тут буде помилка недостачі аргументів)"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('abc', '1', '23')
describe_pet()
