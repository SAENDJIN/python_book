names = ['sasha', 'andrey', 'mykita', 'vlad', 'masha']
print(names[0:3])
print(names[1:4])
print(names[2:5])
print(names[:5])
print(names[0:])
print(names[-3:])
print(names[:-2]) #больная хуйня с отзеркаливанием
print(names[:])

print('Here first three players:')
for player in names[:3]:
    print(player.title())

names_of_people_from_canada = names[:]
print(names_of_people_from_canada)

names.append('Veronika')
names_of_people_from_canada.append('Lera')

print(names_of_people_from_canada)
print(names)