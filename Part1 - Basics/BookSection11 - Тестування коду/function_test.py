from function_for_test import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input(f'\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input(f'\nPlease give me a last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNearly formatted name: {formatted_name}.")
