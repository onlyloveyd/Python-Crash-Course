current_users = ['admin', 'Bob', 'Tom', 'Joe', 'James']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

new_users = ['BOB', 'Curry', 'Ana', 'Ame', 'JOE']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'{user} is already is use')
    else:
        print(f'{user} is a new user')
