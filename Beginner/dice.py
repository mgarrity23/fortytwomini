import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def setSides(self, new_sides):
        self.sides = new_sides

    def getSides(self):
        return self.sides

    def roll(self):
        return random.randint(1, self.sides)


dice = Dice(6)
dice2 = Dice(6)

B = [0] * 12
for i in range(100000):
    total = dice.roll() + dice2.roll()
    B[total-1] += 1

print(B[1:])
