# 8-12

def make_sandwich(*ingradients):
    """Виводить замовлені інградієнти для сендвічу"""
    print(f"\nMake sandwich with this ingredients:")
    for ingredient in ingradients:
        print(ingredient.title())


make_sandwich('cheese', )
make_sandwich('red pepper', 'cheese')
make_sandwich('pepperoni', 'cheese', 'red pepper')


# 8-13

def build_profile(first, last, **user_info):
    """"Створити словник, що міститиме всю інформацію про користувача."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'Andrii',
    'Saienko',
    location='Kyiv',
    field='General QA',
    height=180
)
print(user_profile)


# 8-14

def make_car(manufacturer, model, **kwargs):
    """"Створити словник, що міститиме всю інформацію про автомобіль."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


toyota_car = make_car(
    'toyota',
    'supra',
    engine='2jz',
    doors=3
)
mazda_car = make_car(
    'mazda',
    'rx7',
    engine='rotor',
    doors=3
)
subaru_car = make_car(
    'subaru',
    'imprezza wrx sti',
    engine='b18',
    doors=5
)

print(toyota_car)
print(mazda_car)
print(subaru_car)
