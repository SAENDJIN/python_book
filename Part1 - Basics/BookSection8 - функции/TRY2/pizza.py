def make_pizza(size, *toppings):
    print(f'\nMake a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f"-{topping}")

#
# make_pizza(16, 'papperoni')
# make_pizza(22, 'extra cheese', 'peppers', 'chili')