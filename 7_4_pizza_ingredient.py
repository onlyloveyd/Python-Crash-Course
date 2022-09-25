prompt = "Pls input a series of ingredient?\n"
active = True
QUIT = 'quit'
while active:
    name = input(prompt)
    print(name)
    if name == QUIT:
        break
    # active = name.lower() != QUIT
