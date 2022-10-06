from random import randint, choice

print(randint(10, 100))

players = ['andrii', 'oleg', 'timur', 'rostik', 'maria', 'olga']
first_up = choice(players)
print(first_up.title())
