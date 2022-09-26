file_path = 'pg69043.txt'
try:
    with open(file_path) as file_object:
        content = file_object.read()
        the_count = content.lower().count('the')
        accurate_the_count = content.lower().count('the ')
        print(f'the count= {the_count}')
        print(f'accurate the count= {accurate_the_count}')
except FileNotFoundError:
    print('No source file')
else:
    pass
