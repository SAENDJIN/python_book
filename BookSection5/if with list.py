# requested_toppings = ['mushroms', 'green pepper', 'extra cheese']
# requested_toppings = []
#
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green pepper':
#         print(f'Sorry green pepper is ended.')
#     else:
#         print(f'Adding {requested_topping}.')
#
# print(f'\nFinnished making your pizza')

# ------------------------------

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_topping}')
#     print(f'\nFinnished making your pizza')
# else:
#     print('are u sure you want empty pizza?')

# ------------------------------

available_toppings = ['mushrooms', 'olives', 'red pepper',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Add {requested_topping}.")
    else:
        print(f"Sorry we dont have {requested_topping}")
print('\nFinnished making your pizza')
