########################################################################
# generate a random number
# user has to guess the random number generated and will input via console
# then compare the output and input - indicate whether the guess is too
# high or low , if correct give a positive indication
# lets say we give him 3 chances and break the function
########################################################################

import random


def generate_random(min, max):
    generated = random.sample(range(min, max), 1)
    for i in generated:
        return i


def user_guess():
    guess = int(input('enter guess:'))
    return guess


def main(min, max):
    generated = generate_random(min, max)
    count = 0
    while(count < 3):
        guess = user_guess()
        if abs(generated - guess) != 0:
            print('then number is incorrect')
            count += 1
        else:
            print('hurray you have guessed the right number')
            break
    else:
            print('you have reached maximum attempts')
            print('correct answer is %d', generated)


main(1, 6)
