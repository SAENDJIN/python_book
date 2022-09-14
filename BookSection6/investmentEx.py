# 6-7

# friend_Mykyta = {
#     'name': 'Mykita',
#     'surname': 'Kovalsky',
#     'age': 22,
#     'city': 'Kyiv'
# }
# friend_Vlad = {
#     'name': 'Mykita',
#     'surname': 'Kolomiets',
#     'age': 21,
#     'city': 'Kyiv'
# }
# friend_Sasha = {
#     'name': 'Sasha',
#     'surname': 'Kuzmenko',
#     'age': 21,
#     'city': 'Kyiv'
# }
#
# people = [friend_Sasha, friend_Vlad, friend_Mykyta]
# for abc in people:
#     print(abc)

# 6-8

# pet_1 = {'Beagle', 'Oleg'}
# pet_2 = {'Old English Sheepdog', 'Andrii'}
# pet_3 = {'Eurasier', 'Alex'}
#
# pets = [pet_1, pet_3, pet_2]
# for breed, owner in pets:
#     print(f"{breed} is {owner} Dogs")

# 6-9

# favorite_places = {
#     'Andrii': ['home', 'restaurant', 'work'],
#     'Mykyta': ['Lviv'],
#     'Veronika': ["Andrii's home", 'restaurant'],
# }
# for name, places in favorite_places.items():
#     if len(places) > 1:
#         print(f"{name}'s favorite places are:")
#         for place in places:
#             print(f"\t-{place.title()}")
#     else:
#         print(f"{name}'s favorite places is: \n\t-{place.title()}")

# 6-10

# friends_fav_num = {
#     'Mykita': [10, 21, 25],
#     'Maria': [22, 55, 99],
#     'Oleg': [4],
#     'Andrii': [31, 3228, 777]
# }
#
# for name, nums in friends_fav_num.items():
#     if len(nums) > 1:
#         print(f"{name}'s favorite nums are:")
#         for num in nums:
#             print(f"\t{num}")
#     else:
#         print(f"{name}'s favorite places is: \n\t{num}")

# 6-11

# cities = {
#     'Kiev': {
#         'country': 'Ukraine',
#         'population': '43,165,435',
#         'president': 'Zelensky',
#     },
#     'Warsaw': {
#         'country': 'Poland',
#         'population': '37,755,903',
#         'president': 'Duda',
#     },
#     'moscow': {
#         'country': 'ruzzia',
#         'population': '146,071,893',
#         'president': 'putin',
#     },
# }
# for city, city_info in cities.items():
#     print(f"\nCity: {city}")
#     country = city_info['country']
#     population = city_info['population']
#     president = city_info['president']
#     print(f"\tThis city is capital of {country}, with {population} population. And president "
#           f"of this country is {president}")

# 6-12
# make earlier
