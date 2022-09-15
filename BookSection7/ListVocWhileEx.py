# 7-8

sandwich_orders = ['burger', 'chicken burger', 'fich burger', 'vegan not burger', ]
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Make your {current_sandwich} now!")

    finished_sandwich.append(current_sandwich)

print("This sandwiches are ready to go")
for sandwich in finished_sandwich:
    print(sandwich.title())

# 7-9

sandwich_orders = ['burger', 'chicken burger', 'fich burger', 'pastrami sandwich', 'vegan not burger',
                   'pastrami sandwich', 'pastrami sandwich', ]
finished_sandwich = []

print("We so sorry but pastrami sandwiches are ended")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Make your {current_sandwich} now!")

    finished_sandwich.append(current_sandwich)

print("This sandwiches are ready to go")
for sandwich in finished_sandwich:
    print(sandwich.title())

# 7-10

responses = {}

polling_active = True

while polling_active:
    user = input("\nHey, whats your name? ")
    response_place = input("\nWhat place do you want to visit in world ")
    response_person = input("\nWho you take with you? ")
    final_response = f"{response_place} with {response_person}"
    responses[user] = final_response

    repeat = input("Would you like to another person respond? (Y/N)")

    if repeat == 'Y':
        polling_active = True
    elif repeat == 'N':
        polling_active = False
    elif repeat != 'Y' or 'N':
        print("Print 'Y' or 'N'")

print("\n--- Poll result ---")
for user, final_response in responses.items():
    print(f"{user.title()} would visit {final_response}")