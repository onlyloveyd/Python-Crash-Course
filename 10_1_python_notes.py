file_path = 'learning_python.txt'
with open(file_path) as file_object:
    content = file_object.read()
print(content)

with open(file_path) as file_object:
    for line in file_object:
        print(line)

with open(file_path) as file_object:
    lines = file_object.readlines()
print(lines)
