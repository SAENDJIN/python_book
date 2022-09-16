# 4-10
names = ['glass', 'micro', 'mouse', 'vape', 'book', 'powerbank']
print(f'first three item in this line are: {names[:3]}')
print(f'three item at the middle of this line are: {names[2:5]}')
print(f'the last three item in this line are: {names[-3:]}')

# 4-11
my_fav_pizzas = ["Hawaiian", "Barbecue", "Four cheeses"]
friends_fav_pizzas = my_fav_pizzas[:]

print(my_fav_pizzas)
print(friends_fav_pizzas)

my_fav_pizzas.append('Texas')
friends_fav_pizzas.append('Paperoni')
for my_fav_pizza in my_fav_pizzas:
    print(f'My fav pizza is: {my_fav_pizza}')
print(f'\n')
for friends_fav_pizza in friends_fav_pizzas:
    print(f'Friend fav pizza is: {friends_fav_pizza}')
print(friends_fav_pizzas)

# 4-12
foods = ['apple', 'pancake', 'tomato', 'water', 'coce']
for food in foods:
    print(f"I like item like this: {food}!")
