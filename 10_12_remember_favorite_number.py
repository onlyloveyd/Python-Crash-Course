import json

json_path = 'favorite_number.json'


def get_favorite_number():
    try:
        with open(json_path) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def store_favorite_number():
    favorite_number = get_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! it's {favorite_number}")
    else:
        favorite_number = input('What is your favorite number: ')
        with open(json_path, 'w') as f:
            json.dump(favorite_number, f)


store_favorite_number()
