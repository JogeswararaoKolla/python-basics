import random


def roll_dice():
    dice_total = 0
    for i in range(2):
        roll = random.randint(1, 6)
        dice_total = dice_total + roll
        print("Roll Dice #", i, roll)
    return dice_total


guess = int(input('Guess the dice roll:\n'))
result = roll_dice()
if guess == result:
    print("You win")
else:
    print("You Loose Computer dice roll is ", result)
