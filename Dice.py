'''This program will roll dice'''

#import modules
import random

#define min and max numbers on dice
#define how many dice
min = 1
max = int(input('How many sides should be on the dice?'))
dice = int(input('How many dice shall I roll?'))

#play again variable
rollAgain = 'yes'

#rolling the dice while loop
while rollAgain == 'yes' or rollAgain == 'y':
print('Rolling the Dice!')
print('The Dice are...')
for number in range(0, dice):
number_current = random.randint(min, max)
print(number_current)
print('Do you want to roll again?')
rollAgain = input(': ')
'''This program will roll dice'''

#import modules
import random

#define min and max numbers on dice
#define how many dice
min = 1
max = int(input('How many sides should be on the dice?'))
dice = int(input('How many dice shall I roll?'))

#play again variable
rollAgain = 'yes'

#rolling the dice while loop
while rollAgain == 'yes' or rollAgain == 'y':
print('Rolling the Dice!')
print('The Dice are...')
for number in range(0, dice):
number_current = random.randint(min, max)
print(number_current)
print('Do you want to roll again?')
rollAgain = input(': ')
