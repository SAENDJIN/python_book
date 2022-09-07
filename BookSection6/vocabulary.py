# alien_0 = {'colour': 'green', 'points': 5}
#
# print(f'Colour of alien is: {alien_0["colour"]}')
# print(alien_0['points'])

# ------------------------------------------

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# ------------------------------------------

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# ------------------------------------------

# alien_1 = {}
#
# alien_1['colour'] = 'red'
# alien_1['points'] = 10
#
# print(alien_1)

# ----------------------------------------

# alien_3 = {'colour': 'green'}
# print(f'Colour of alien is: {alien_3["colour"]}')
#
# alien_3['colour'] = 'yellow'
# print(f'Colour of alien now is: {alien_3["colour"]}')

# ------------------------------------------

# alien_4 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_4['x_position']}, {alien_4['y_position']}")
#
# if alien_4['speed'] == 'slow':
#     x_increment = 1
# elif alien_4['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_4['x_position'] = alien_4['x_position'] + x_increment
#
# print(f"New position: {alien_4['x_position']}, {alien_4['y_position']}")

# ---------------------------------------------

# alien_5 = {'colour': 'green', 'points': 5}
# print(alien_5)
#
# del alien_5['points']  # del удаляеть на всегда!
# print(alien_5)

# ------------------------------------------

# favorite_language = {
#     'Andrii': 'python',
#     'Mykita': 'JS',
#     'Vlad': 'python',
#     'Oksana': 'Java',
# }
#
# language = favorite_language['Andrii'].title()
# print(f"Andrii favs lang is {language}")

# ---------------------------------------

# alien_6 = {'colour': 'green', 'points': 5, }
# speed_value = alien_6.get('speed', 'No speed assigned')  # Если нет в словаре "Speed" то он укажет сообщение,
# # если есть, значение с словаря
# print(speed_value)
