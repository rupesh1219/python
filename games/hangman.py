###############################################################################
# hangman game
# given list of famous cities
# guess the word by inputing the letters one by one
# allow the user to input only limited inputs
###############################################################################


###############################################################################
# game steps:
# welcome the user to the game
# and introduce hime to the what part of game he is playing
# then ask him to predict the n letter word city of tech
# once that is predicted correct remove it from the list for a game
# if given wrong inputs through to user this is wrong input
# repeat the game until he wants to play if he doesnt want to play quit
# if he continues quit the game after selecting all the cities
# thank him for playing the game
###############################################################################

list_of_famous_cities = ['newyork', 'sanfranciso', 'chicago', 'dallas',
                         'florida', 'seattle']


def welcome():
    print('welcome to the hangman')
    print('today you will guess the top 7 tech cities')


def city_of_length():
    '''
    from a dictionary where
    the key is length and value
    is city
    '''
    print(list_of_famous_cities)
    dict_items = {}
    for i in list_of_famous_cities:
        dict_items[len(i)] = i
    print(dict_items)
    return dict_items


def ask_question():
    '''
    predict the n letter city
    '''
    city_lengths = city_of_length()
    print(city_lengths)
    counter = 0
    while counter <= 10:
        input_from_user = input('enter a length tech city')
        if input_from_user in city_lengths.values():
            return 'predicted correct tech city, you are fabulous'
        else:
            counter += 1
            print('wrong answer')
    else:
        return 'you are hanged'


print(welcome())
print(ask_question())
