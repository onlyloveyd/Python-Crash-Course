number_one = 0
number_two = 0

while True:
    try:
        number_one = int(input('Pls input a number: '))
    except ValueError:
        print('Not a number')
        continue
    else:
        break

while True:
    try:
        number_two = int(input('Pls input another number: '))
    except ValueError:
        print('Not a number')
        continue
    else:
        break

print(f'{number_one}+{number_two} = {number_one + number_two}')
