term = {
    'nile': 'egypt',
    'yangtze': 'china',
    'yellow': 'china',
    'mississippi': 'american',
}
for key, value in term.items():
    print(f'The {key.title()} runs through {value.title()}')

for value in set(term.values()):
    print(value.title())