def get_formatted_name(first, last, middle=''):
    """Згенерувати відформатоване повне ім'я"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
