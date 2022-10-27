# 10-3 Гість

# filename = "file_directory/guest.txt"
#
# guest_name = input("Hey, tell your name:\n")
# with open(filename, 'a') as file_object:
#     file_object.write(guest_name)

# 10-3 Гість upgraded (Майже 10-4)

# filename = "file_directory/guest.txt"
# guest_list = []
#
# guest_name = input("Hey, tell your name:")
# guest_list.append(guest_name)
#
# with open(filename, 'a') as file_object:
#     for name in guest_name:
#         file_object.write(f"{name}")
#     file_object.write("\n")

# 10-4 - Гостьова книга

# filename = "file_directory/guest_book.txt"
#
# print("Enter 'quit' when you are finished")
# while True:
#     name = input("\nWhat is your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as f:
#             f.write(f"{name}\n")
#         print(f"Hi ,{name}, you've been added to the guest book ")

# 10-5 Опитування про програмування

filename = "file_directory/programming_reason_list.txt"

print("Enter 'quit' when you are finished")
while True:
    reason = input("\nWhy you like programming? ")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{reason}\n")
        print(f"Any other reasons? ")
