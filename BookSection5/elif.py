age = 18
if age <= 4:
    price = 0
elif age <= 18:
    price = 10
elif age >= 65:
    price = 10
elif age > 18:
    price =35
print(f'Ticket price {price}')

requested_toppings = ['ananas', 'onion', 'mushrooms', 'pepperoni']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'сheese' in requested_toppings:
    print("Adding сheese.")

print("\nFinished making your pizza!")
