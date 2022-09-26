cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(cats_file) as cats_objects:
        print(cats_objects.read().rstrip())
    with open(dogs_file) as dogs_objects:
        print(dogs_objects.read().rstrip())
except FileNotFoundError:
    print("File Not Found")
else:
    print("Read Successfully")
