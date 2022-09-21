def make_pizza(size, *toppings):
    """Описати піцу яку ми збираємось приготувати"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


def test():
    print('test')
