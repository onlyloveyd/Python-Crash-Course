from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


"""Side 6"""
print("\nSide 6")
dice = Die(6)
for i in range(1, 11):
    dice.roll_die()

"""Side 10"""
print("\nSide 10")
dice = Die(10)
for i in range(1, 11):
    dice.roll_die()

"""Side 20"""
print("\nSide 20")
dice = Die(20)
for i in range(1, 11):
    dice.roll_die()
