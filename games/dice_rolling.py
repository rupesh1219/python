########################################################################
# main aim of this project is to roll a dice and print the outcome
# you can select your own number of faces to a dice, normally a general
# dice has 1 and 6 has min and max values. And user should be asked to
# roll the dice again or not when a roll is completed
########################################################################


'''
steps:
1. decide number of faces to a dice
2. then select a max and min value based on the above step
3. roll a dice and print the output
4. ask the user to roll a dice again
'''

import random


def welcome():
    '''
    welcome function
    '''
    print('welcome to the dice game')


def output(max, min):
    '''
    output when dice is rolled
    '''
    print(random.sample(range(max, min), 1))


def roll_dice(max, min):
    '''
    roll a dice and
    print output
    '''
    while True:
        ask = input('do you want to roll a dice?')
        if ask == 'yes':
            output(max, min)
        else:
            print(' thank you for playing with us')
            break


welcome()
roll_dice(1, 7)

'''
if you want to play with two dice just increae the second
argument of the random.sample function
'''
