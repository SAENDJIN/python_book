# alien_0 = {'colour': 'green', 'points': 5}
# alien_1 = {'colour': 'yellow', 'points': 10}
# alien_2 = {'colour': 'red', 'points': 15}
# alien_3 = {'colour': 'purple', 'points': 25}
#
# aliens = [alien_0, alien_1, alien_2, alien_3]
#
# for alien in aliens:
#     print(alien)

# ------------------------------

# aliens = []
#
# for alien_number in range(30):
#     new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:3]:
#     if alien['colour'] == 'green':
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#         alien['colour'] = 'yellow'
#     elif alien['colour'] == 'yellow':
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#         alien['colour'] = 'red'
# for alien in aliens[:5]:
#     print(alien)
# print('....')
# print(f"Total number of aliens: {len(aliens)}")

# ------------------------------

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'exta cheese'],
# }
# print(f"You order a {pizza['crust']}-crust pizza with the following topings:")
# for topping in pizza['toppings']:
#     print(f'\t + {topping}')

# ------------------------------

favorite_language = {
    'Andrii': ['python', 'Java'],
    'Mykyta': ['C#', 'Java'],
    'Vlad': ['python', 'Java'],
    'Oksana': ['Java', 'JS'],
    'Veronika': ['Java', 'python'],
    'Lena': ['python'],
}

for name, languages in favorite_language.items():
    if len(languages) > 1:
        print(f"{name}'s favorite language are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"{name}'s favorite language is:\n\t{language.title()}")

# ------------------------------

users = {
    'SAENDJIN': {
        'firstname': 'Andrii',
        'lastname': 'Saienko',
        'location': 'Kyiv',
    },
    'N33K': {
        'firstname': 'Mykyta',
        'lastname': 'Kovalski',
        'location': 'Kyiv',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['firstname']} {user_info['lastname']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")