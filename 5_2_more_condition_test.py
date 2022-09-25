hello = "Hello"
world = "World"
print(hello == 'Hello')
print(hello == world)

print(hello == 'hello')
print(hello.lower() == 'hello')

score = 60
print(score < 60)
print(score == 60)
print(score > 60)

print(hello.lower() == 'hello' and score == 60)
print(hello == 'hello' or score < 60)

pizzas = ['Seafood', 'Sausage', 'Cheese']
print('seafood' in pizzas)
print('Seafood' in pizzas)
