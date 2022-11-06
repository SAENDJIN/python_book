import json, gettext

with open('texts_ua_en_ru/language.json', encoding='utf-8') as lg:
    lang = json.loads(lg.read())

print(f"Welcome to our tech / game shop!")
print(f"We propose you to choose language that most convenient to you.")

# class Lang
def choose_language():
    """Обирає при першому вході мову та валюту користувача"""
    language = input("Print 'UA' to use Ukrainian language "
                     "\nPrint 'EN' to use English language "
                     "\nPrint 'RU' to use Russian language "
                     "\nLanguage: ")
    if language == 'UA':
        chosen_language = lang['ua']['welcome message']
        print(chosen_language)
    elif language == 'EN':
        chosen_language = lang['en']['welcome message']
        print(chosen_language)
    elif language == 'RU':
        chosen_language = lang['ru']['welcome message']
        print(chosen_language)
    else:
        print("Sorry, we don't understand text. Choose language from next list.")
        choose_language()


def choose_currency():
    language =

