prompt = "Pls enter your age:\n"
active = True
QUIT = 'quit'
while active:
    name = input(prompt)
    if name == QUIT:
        break
    name = int(name)
    if name < 3:
        print('Free')
    elif name < 12:
        print('$10')
    else:
        print('$15')
