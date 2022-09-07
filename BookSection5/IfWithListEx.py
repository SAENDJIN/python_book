# # 5-8
#
# names = ['andrii', 'veronika', 'mykita', 'lena', 'admin']
#
# for name in names:
#     if name == 'admin':
#         print(f'Hello {name}, would u like to see status report')
#     else:
#         print(f'Hello {name.title()}, thank u for loggin again')

# # 5-9
#
# names = ['andrii', 'veronika', 'mykita', 'lena', 'admin']
# if names:
#     for name in names:
#         if name == 'admin':
#             print(f'Hello {name}, would u like to see status report')
#         else:
#             print(f'Hello {name.title()}, thank u for loggin again')
# else:
#     print('We need some users')

# # 5-10
# # current_users = ['SAENDJIN', 'N33K', 'urkasauron',
# #                  'MamoruKuzuma', 's1mple', 'admin']
# current_users = ['saendjin', 'n33k', 'urkasauron',
#                  'MamoruKuzuma', 's1mple', 'admin']
# new_users = ['user1', 'SAENDJIN', 'saendjin', 'user4', 'N33K']
#
#
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f'Username: {new_user} is already taken')
#     else:
#         print(f'U can use this:"{new_user}" username ')

# 5-11

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
