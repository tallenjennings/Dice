"""This program will roll dice"""

#Import modules
import random

#define dice function
def dice():
    try:
        #Define min and max numbers on dice
        min = 1
        max = int(input('How many sides should be on the dice?'))
        
        #Define how many dice
        dice = int(input('How many dice shall I roll?'))

        #Rolling the dice while loop
        print('Rolling the Dice!')
        print('The Dice are...')
        for number in range(0, dice):
            print(random.randint(min, max))
    except ValueError as error:
        print('That is not a valid selection!?!')


#Calling the dice game
rollAgain = 'y'
while rollAgain == 'y':
    dice()
    rollAgain = input('Do you want to roll again?y/n:')
    if rollAgain == 'n':
        break


