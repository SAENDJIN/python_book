def make_pizza(*toppings):
    """Скласти список замовлених інгредієнтів"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# ------------------------------

def make_pizza(size, *toppings):
    """Описати піцу яку ми збираємось приготувати"""
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(topping)


make_pizza(16, 'pepperoni')
make_pizza(21, 'mushrooms', 'green peppers', 'extra cheese')


# ------------------------------

def build_profile(first, last, **user_info):
    """"Створити словник, що міститиме всю інформацію про користувача."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'alber',
    'einstein',
    location='princeton',
    field='physics',
)
print(user_profile)
