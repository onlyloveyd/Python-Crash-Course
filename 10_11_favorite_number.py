import json

json_path = 'favorite_number.json'
favorite_number = input('Pls input your favorite number: ')
with open(json_path, 'w') as f:
    json.dump(favorite_number, f)

with open(json_path) as f:
    print(f"I know your favorite number! it's {json.load(f)}")
