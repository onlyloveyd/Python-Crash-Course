cities = {
    'XiAn': {
        'country': 'China',
        'population': 100000,
        'fact': 'Beautiful'
    },
    'NewYork': {
        'country': 'American',
        'population': 12,
        'fact': 'Modern'
    },
    'Kuala Lumpur': {
        'country': 'Singapore',
        'population': 50000,
        'fact': 'Fashion'
    },
}

for key, value in cities.items():
    print(f'{key}:{value}')
