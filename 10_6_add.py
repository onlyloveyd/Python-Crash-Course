one = input('Pls input a number: ')
two = input('Pls input another number: ')

try:
    number_one = int(one)
    number_two = int(two)
except ValueError:
    print('Pls input number')
else:
    print(f'{number_one}+{number_two} = {number_one + number_two}')
