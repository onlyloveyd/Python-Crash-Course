prompt = 'If you could visit one place in the world, where would you go?\n'
active = True
QUIT = 'quit'
results = []
while active:
    place = input(prompt)
    if place == QUIT:
        break
    else:
        results.append(place)

print(results)
