guest_number = input('How many guests?\n')
guest_number = int(guest_number)

if guest_number > 8:
    print('No tables')
else:
    print('Tables available!')
