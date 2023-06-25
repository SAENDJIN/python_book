def greet_users(names):
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)


usernames = ['andrii', 'oleh', 'veronika']
greet_users(usernames)
