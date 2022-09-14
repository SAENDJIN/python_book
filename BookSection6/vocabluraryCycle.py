# user_0 = {
#     'username': 'SAENDJIN',
#     'first': 'andrii',
#     'last': 'saienko',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"\nValue: {value}")

# ------------------------------

# favorite_language = {
#     'Andrii': 'python',
#     'Mykyta': 'C#',
#     'Vlad': 'python',
#     'Oksana': 'Java',
# }
#
# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}!")
#
# for name in favorite_language.keys():
#     print(name.title())

# ------------------------------

# favorite_language = {
#     'Andrii': 'python',
#     'Mykyta': 'C#',
#     'Vlad': 'python',
#     'Oksana': 'Java',
# }
#
# friends = ['Vlad', 'Mykyta']
# for name in favorite_language.keys():
#     print(name.title())
#
#     if name in friends:
#         language = favorite_language[name].title()
#         print(f"\t{name.title()}, I see you love {language}")

# ------------------------------

# favorite_language = {
#     'Andrii': 'python',
#     'Mykyta': 'C#',
#     'Vlad': 'python',
#     'Oksana': 'Java',
# }
#
# if 'veronika' not in favorite_language.keys():
#     print('Veronika, pls take out pull')

# ------------------------------

# favorite_language = {
#     'Andrii': 'python',
#     'Mykyta': 'C#',
#     'Vlad': 'python',
#     'Oksana': 'Java',
#     'Veronika': 'Java',
#     'Lena': 'python',
# }
#
# for name in sorted(favorite_language.keys()):
#     print(f"{name.title()}, thank you for takin the pull")
#
# for language in favorite_language.values():
#     print(language.title())

# ------------------------------

favorite_language = {
    'Andrii': 'python',
    'Mykyta': 'C#',
    'Vlad': 'python',
    'Oksana': 'Java',
    'Veronika': 'Java',
    'Lena': 'python',
}
for language in set(favorite_language.values()):
    print(language.title())

# ------------------------------
