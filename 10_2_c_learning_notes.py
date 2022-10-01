file_path = 'learning_python.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line.replace('Python', 'Kotlin'))
