# 10-1
# file_name_ex = 'file_directory/learning_python.txt'
#
# print(f"\n---Reading the entire file: \n")
#
# with open(file_name_ex) as file_object:
#     contents = file_object.read()
# print(contents)
#
# print(f"\n---Looping over the lines \n")
#
# with open(file_name_ex) as file_object:
#     for line in file_object:
#         print(line.rstrip())
#
# print(f"\n---Storing the lines as list:\n")
# with open(file_name_ex) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())

# 10-2

file_name_ex_2 = 'file_directory/learning_python.txt'

print(f'Original message in file: ')

with open(file_name_ex_2) as file_object_2:
    message = file_object_2.read()
print(message)

print(f'\nEdited message from file:')

with open(file_name_ex_2) as file_object_2:
    message_2 = file_object_2.read()
    message_edited = message_2.replace('python', "'C'")
print(message_edited)
