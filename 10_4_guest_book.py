file_path = 'guest_book.txt'

QUIT = 'quit'
while True:
    name = input('Pls input you name: ')
    if name.lower() == QUIT:
        break
    print(f"Hello {name}")
    with open(file_path, 'a') as file_object:
        file_object.write(name + '\n')
