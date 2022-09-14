# 6-4

# glossary = {
#     'if': 'Условие "если"',
#     'else': 'Если не сработало условие "if", выполняет условие тогда',
#     'print': 'Выводит текст',
#     'get': 'Если чего-то не хватает, он укажет заданое вами значение',
#     'tittle': 'Делает вывод с большой буквы',
#     'for': 'Перебирает все значения и выполняет цикл',
#     'items()': 'из словаря берет ключ и значени',
#     'keys()': 'из словаря берет ключ',
#     'value()': 'из словаря берет значение',
#
# }
#
# for command, action in glossary.items():
#     print(f"This command '{command}' make this action - {action}")

# 6-5

# rivers = {
#     'Amazon': 'Brazil',
#     'Nile': 'Uganda',
#     'Mississipp': 'United States',
#     'Yellow River': 'China'
# }
#
# for river, country in rivers.items():
#     print(f"{river.title()} runs through {country.title()}")
# for river in rivers.keys():
#     print(river)
# for country in rivers.values():
#     print(country)

# 6-6

# favorite_language = {
#     'Andrii': 'python',
#     'Mykyta': 'C#',
#     'Vlad': 'python',
#     'Oksana': 'Java',
#     'Veronika': 'Java',
#     'Lena': 'python',
# }
# pull_people = ['Andrii', 'Mykola', 'Olga', 'Lena']
#
# for person in pull_people:
#     if person not in favorite_language.keys():
#         print(f"{person} pls pull your language")
#     else:
#         print('Thx for voting')
