pizzas = ['Seafood', 'Sausage', 'Cheese']
friend_pizzas = pizzas[:]

pizzas.append('Beef')
friend_pizzas.append('Corn')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
