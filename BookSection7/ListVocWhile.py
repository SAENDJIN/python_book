# unconfirmed_users = ['alice', 'braian', 'andrii']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# ------------------------------

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# ------------------------------

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to another person respond? (Y/N)")

    if repeat == 'Y':
        polling_active = True
    elif repeat == 'N':
        polling_active = False
    elif repeat != 'Y' or 'N':
        print("Print 'Y' or 'N'")

print("\n--- Poll result ---")
for name, response in responses.items():
    print(f"{name}, would like to climb {response}.")
