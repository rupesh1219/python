########################################################################
# PRACTICE ON STRINGS FROM W3SOURCE SCHOOLS
#######################################################################

# write a program to give the character frequency in a string

n = input('enter a string:')

def str_freq():
    dict = {}
    for i in n:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(str_freq())

########################################################################

# write a program to return first 2 and last2  characters of a string '
# if length is greater than or equal to 2 or else return empty string

n = (input('enter a string:'))

def str_ret():
    if len(n) >= 2:
        return n[:2]+n[-2:]
    else:
        return 'empty string'

print(str_ret())

########################################################################

# write a program to repalce the first character ocuurence in the string
# with $

n = input('enter a string:')

def first_ocu():
    s = ''
    for i in range(len(n)):
        if n[i] == n[:1] and i > 0:
            s += '$'
        else:
            s += n[i]
    return s

print(first_ocu())

########################################################################

# write a program to return a single string from two strings separated
# by space on excahging the first two characters of two strings

m = input('enter a string:')
n = input('enter a string:')

def ret_com():
    return n[:-1]+m[-1:] + ' ' + m[:-1]+n[-1:]

print(ret_com())

########################################################################

# add ing to the end of the string is >3 length and if hte string already
# has ing then add ly, if len is <3 just return the string

n = input('enter the string:')

def ret_str():
    if len(n) > 3 and n[-3:] == 'ing':
        return n+'ly'
    elif len(n) > 3 and n[-3:] != 'ing':
        return n + 'ing'
    else:
        return n

print(ret_str())
########################################################################

# write a python program to read the list of words and print the longest
# one from the list

n = int(input('enter the max range of list:'))

def list_words():
    l = []
    for i in range(n):
        l.append(input('enter the word:'))
    return l

def print_longest():
    l = list_words()
    j = 0
    temp = 0
    for i in l:
        j = len(i)
        if j > temp:
            temp = j
            word = i
    return word

print(print_longest())

########################################################################

# write a program to count the ocurence of each word in a given sentence

n = input('enter a string:')

words_list = n.split()
print(words_list)

def word_freq():
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        word_count[word] = 1
    return word_count

print(word_freq())

########################################################################

# write a program that accepts the comma separate sequence of words
# and arrange them in sorted order with unique elements

n = input('enter comma separated sequcne:'.split(','))
print(n)

# read the above sequence in to a list

l = n.split(',')
print(l)
m = list(set(l))
print(m)
#set is already an ordered collection and has unique elements

########################################################################

# write a python function to create an HTML string with tags around the
# words.

def html_tags(a, b):
    return '<' + a + '>' + b + '<' + '/' + a + '>'

print(html_tags('i', 'python_learning'))

########################################################################

# write a python function to insert a string in middle of a string

def insert_middle(a, b):
    if len(a) % 2 == 0:
        return a[:int(len(a)/2)] + b + a[int(len(a)/2):]
    else:
        return 'cant insert the string exactly in the middle'

print(insert_middle('[[]]', 'python'))

########################################################################

# write a python function to convert the whole string in to uppercase
# if any two characters in first 4 letters are uppercase

def upper_case(n):
    count = 0
    for i in range(4):
        if n[i] == n[i].upper():
            count += 1
    return count

def result_needed(n):
    count1 = upper_case(n)
    if count1 >=2:
        return n.upper()
    return n

print(result_needed('rupEsh'))

########################################################################

# write a python program to sort a string lexicographically

n = input('enter a string:')

#convert str to list
def str_list():
    l = ''.join(sorted(n))
    return l

print(str_list())

########################################################################

# write a python program to implement Ceaser's Cryptography'
# this can easily be done using ascii character and value conversions
# ord and chr functions are used to conver the values in to ascii and char

p = int(input('creating the rule:'))

n = input('enter a string:')

def encrypted_msg():
    m = ''
    for i in range(len(n)):
        m[i] == n[i+p]

########################################################################
