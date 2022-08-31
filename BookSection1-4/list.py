# emails = ['andrey.saenko31@gmail.com', 'andrii.qa31@gmail.com']
# friends = ['Влад', 'Никита', 'Маша', 'Саша', 'Влад(Маши)']
# cars = ['honda', 'mazda', 'toyota', 'audi']
consoles = ['Playstation', 'Playstation 2', 'Playstation 3', 'Playstation 4', 'Playstation 5']

# friend_message = f'Вот список моих друзей по порядку:\n1. {friends[1]} \n2. {friends[2]}'
# print(friend_message)
# friend_rofl = f'Вот они мои друзья слева на право {friends[0]}, {friends[1]}, {friends[2]},' \
#               f' {friends[3]}, {friends[4]}'
# print(friend_rofl)

# print(emails[1][2])
# в случае -1 испрользуеться specialized и вывод дет последних данных из списка
# Можно так же делать с конца и другие значения "-2", "-3" и тд
# print(emails[-1])
# print(emails[-2])

# message = f'My private email is {emails[0]} and my test email is {emails[-1]}'
# print(message)

# print(cars)
# cars[0] = 'honda civic'
# print(cars)
# # 'append' add new value to end of list without changing it
# cars.append('bwm')
# print(cars)
#
# print(consoles)
#
consoles.insert(0, 'Xbox')
consoles.insert(1, 'Xbox 360')
consoles.insert(2, 'Xbox one')
# print(consoles)
# # 'del' - delete value in list
#
# del consoles[0]
# print(consoles)
#
# del consoles[-3]
# print(consoles)
#
# 'pop' - cuts out the value but allows it to be used further
consoles_popped = consoles.pop()
consoles_first = consoles.pop(0)

print(consoles)
print(consoles_popped)
#
# firs_owned = consoles_first
# list_owned = consoles_popped
# print(f'My last bought console was {list_owned.title()}')
# print(f'My first bought console was {firs_owned.title()}')


# print(consoles)
# consoles.remove('Xbox')
# print(consoles)
# 'remove' - remove value by name (delete only one value, if u have more than one u should create cycle
# piece_off_shit = 'Xbox'
# print(consoles)
# consoles.remove(piece_off_shit)
# print(consoles)
# print(f'Delete {piece_off_shit} because its old piece of shit')
