file_path = 'reasons.txt'
QUIT = 'quit'
while True:
    reason = input('Why do you like programming: ')
    if reason == QUIT:
        break
    with open(file_path, 'a') as file_object:
        file_object.write(reason + '\n')
