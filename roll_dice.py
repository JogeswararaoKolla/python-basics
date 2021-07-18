import random
guess = int(input('Guess the dice roll:\n'))
rolldice1 = random.randint(1, 6)
rolldice2 = random.randint(1, 6)
print("Computer rolled Dice1 " + str(rolldice1))
print("Computer rolled Dice2 " + str(rolldice2))
if guess == (rolldice1 + rolldice2):
    print("You win")
else:
    print("You Loose Computer dice roll is " + str(rolldice1 + rolldice2))
