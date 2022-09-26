file_path = 'guest.txt'

name = input('Pls input you name: ')
with open(file_path, 'w') as file_object:
    file_object.write(name)
