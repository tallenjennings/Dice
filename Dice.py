"""This program will roll dice"""

#import modules
import random

#define min and max numbers on dice
#define how many dice
min = 1
max = int(input('How many sides should be on the dice?'))
dice = int(input('How many dice shall I roll?'))

#play again variable
rollAgain = 'y'

#rolling the dice while loop
while rollAgain.lower() == 'y':
    print('Rolling the Dice!')
    print('The Dice are...')
    for number in range(0, dice):
        print(random.randint(min, max))
    rollAgain = str(input('Do you want to roll again?y/n:'))
    if rollAgain == 'n':
        break

