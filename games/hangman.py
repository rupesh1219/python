########################################################################
# hangman game
# given list of famous cities
# guess the word by inputing the letters one by one
# allow the user to input only limited inputs
########################################################################

list_of_famous_cities = ['newyork','california','texas','kansas','florida']


def welcome():
    print('welcome to the hangman')
    print('today you will guess the most beautiful cities')


def ask_city_of_length():
    '''
    ask the user to predict
    7 letter best city
    '''
    list_lengths = []
    for i in list_of_famous_cities:
        list_lengths.append(len(i))
    return list_lengths

def questions():
    '''
    which category of question
    will be asked to the user
    '''
    city_lengths = ask_city_of_length()
    return city_length


def compare():
    '''
    comparing the letter entered
    to the word
    '''
    return

def user_input():
    '''
    user input a letter
    '''
    return

def wrong_input():
    '''
    wrong attempts will make
    the user to exit the game
    '''
    return
