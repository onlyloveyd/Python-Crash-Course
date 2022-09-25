from random import randint

pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd',
        'e']

BINGO = 'baba'
while True:
    result = ''
    for i in range(1, 5):
        result = result + pool[randint(0, 14)]
    if result == BINGO:
        print(f"{result}: BINGO!!!")
        break
    else:
        print(f'{result}: -_- -_- -_-')
        # break
