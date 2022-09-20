def greet_users(names):
    """Вивести просте повідомлення для кожного користувача у списку"""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['andrii', 'oleg', 'vlad', ]
greet_users(usernames)

# ------------------------------

# Почати з креслень, які треба роздрукувати.
unprinted_designs = ['phone case', 'robot', 'tiger toy']
completed_models = []

# Симулювати друк кожного креслення, доки всі не закінчаться
# Перенести кожен рисунок до completed_models після друку
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design.title()}")
    completed_models.append(current_design)

# Показати всі готові моделі

print(f"\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model.title())


# ------------------------------

def print_models(unprinted_designs, completed_models):
    """Симулювати друк кожного креслення, доки всі не закінчаться
    Перенести кожен рисунок до completed_models після друку"""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """"Показати всі надруковані моделі."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot', 'tiger toy']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# print_models(unprinted_designs[:], completed_models[:]) # Создает копии списков