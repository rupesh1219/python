########################################################################
# take input from user and form a story from the inputs
########################################################################


def welcome():
    print('welcome to the type writer \n this will form you a story'
          'for the words given by user')


def user_input(max):
    '''
    take the user input
    and append them into
    a list
    '''
    welcome()
    count = 0
    list = []
    while(count < max):
        ask = input('enter the words:')
        list.append(ask)
        count += 1
    else:
        confirm = input('do you want to add more words:')
        if confirm == 'yes':
            number_words = int(input('how many more words you want to increase'))
            count2 = 0
            while (count2 < number_words):
                ask2 = input('plese enter words:')
                list.append(ask2)
                count2 += 1
    return list


def story(max):
    '''
    print the story from
    input
    '''
    list_items = user_input(max)
    str = ''
    for i in list_items:
        str = str + i
    return str

print(story(10))
