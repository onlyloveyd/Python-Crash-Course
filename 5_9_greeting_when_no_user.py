# users = ['admin', 'Bob', 'Tom', 'Joe', 'James']
users = []
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print('Hello Jaden, thank you for logging in again.')
else:
    print('We need to find some users!')
