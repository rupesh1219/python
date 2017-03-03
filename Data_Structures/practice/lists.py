# practice on lists

# write a python program to print sum of all elements in a list

n = int(input('enter the max elements in a list:'))

def list_entry():
    l = []
    for i in range(n):
        l.append(int(input('enter elements in to list:')))
    return l

def sum_list():
    m = list_entry()
    sum_list = 0
    for i in range(len(m)):
        sum_list += m[i]
    return sum_list

print(sum_list())

########################################################################

# write a python program to multiply all items in a list

def mul_list():
    n = int(input('enter the max len of the list:'))
    l = []
    l = [int(input('enter elements')) for i in range(n)]

    prd_list = 1
    for i in range(n):
        prd_list *= l[i]
    return prd_list

print(mul_list())

########################################################################

# write a function to get the largest element from the list
# define some variables that are required in sorting

n = int(input('enter the max range of the list:'))

def list_gen():
    '''
    function to generate a list
    '''
    l = [int(input('enter elemetns in to list:')) for i in range(n)]
    return l

def bubble_sort():
    '''
    function to do bubble sort
    '''
    l = list_gen()
    while(sorted(l) != l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
        print(l)
    return l # return is a break statement which stops the loop

print(bubble_sort())

########################################################################

# write a program to find the max element of the list using selection
# sort

n = int(input('enter the max range of the list:'))

def list_gen():
    '''
    function to generate a list
    '''
    l = [int(input('enter a list:')) for i in range(n)]
    return l


def selection_sort():
    '''
    function to do selection sort
    '''
    l = list_gen()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j] < l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
        print(l)
    return l

print(selection_sort())

########################################################################

# select max element from the given list and select minimum element of
# the given list

n = int(input('enter the max range of the list:'))

def list_enter():
    '''
    enter the elements
    to the list
    '''
    l = [int(input('enter the list elements:')) for i in range(n)]
    return l

def max_element():
    '''
    selecting the max element from the
    list
    '''
    l = list_enter()
    max_ele = l[0]
    position = 0
    for i in range(1,len(l)):
        if max_ele < l[i]: # by changing this conditino we can c min
            max_ele = l[i]
            position = i
    return max_ele, position

print(max_element())

########################################################################

# sort a list using python by insertion sort

n = int(input('enter range of the list:'))

def list_enter():
    '''
    enter elements
    into list
    '''
    l = [int(input('enter elements into list:')) for i in range(n)]
    return l

def insrtion_sort():
    '''
    sort the list using
    insertion sort which
    takes about O(n**2) time
    '''
    l = list_enter()
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
        print(l)
        for j in range(i, -1):
            if l[j] < l[j-1]:
                temp2 = l[j-1]
                l[j-1] = l[j]
                l[j] = temp2
        print(l)
    return l

print(insrtion_sort())

########################################################################

# write a program to implement merge sort

n = int(input('enter the max range of the list:'))

def list_entr():
    '''
    enter elements
    into list
    '''
    l = [int(input('enter elements into list:')) for i in range(n)]
    return l

# first wrinting a function that divides a list into half
# then apply merge sort algorithm

def list_half():
    l = list_entr()
    l1 = []
    l2 = []

    if len(l)%2 == 0:
        l1 = l[:int(n/2)]
        l2 = l[int(-n/2):]
    return l1,l2

print(list_half())

########################################################################

# print the list of repeating elements

n = int(input('enter elems into list:'))

def list_entr():
    l = [int(input('enter elems into list:')) for i in range(n)]
    return l

def rep_elems():
    l = list_entr()
    m = []
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                m.append(l[i])
        return m

print(rep_elems())

#exact solution

n = int(input('enter range of list:'))

def list_entr():
    '''
    enter elements
    into list
    '''
    l = [int(input('enter elements into list:')) for i in range(n)]
    return l

def non_unique():
    l = list_entr()
    m = []
    for i in range(len(l)):
        if l.count(l[i]) != 1:
            m.append(l[i])
    return m

print(non_unique())
########################################################################

# frequency of a number in a given list

n = int(input('enter the max range of the list:'))

def list_entr():
    l = [int(input('enter elems inot list:')) for i in range(n)]
    return l

def freq_num():
    dict = {}
    l = list_entr()
    for i in l:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(freq_num())

########################################################################

# convert numbers into roman numerals

n = int(input('enter a number to be converted:'))

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dict2 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

def num_to_roman():
    for k,v in dict2.items():
        print(k,v)

num_to_roman()

########################################################################

# return number of strings whose length is 2 or more and the first and
# last element of the string is same

n = int(input('enter max length of the string:'))


def list_entr():
    words = [input('enter the words') for i in range(n)]
    return words


def strings_sol():
    l = list_entr()
    count = 0
    for i in range(n):
        if len(l[i]) >= 2:
                if l[i][0] == l[i][len(l[i])-1]:
                    count += 1
    return count

print(strings_sol())

########################################################################

# write a program to get a list of tuples sorted by the last element in
# the tuple

def merge_sort(list_name):
    '''
    applying merge sort to a list
    of tuples and sorting them by
    the last element
    '''
    if len(list_name) % 2 == 0:


print(tuple_sort([(1,2), (3,4), (2,1), (5,6)]))

def histogram(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(histogram([1,1,2,2,3]))

########################################################################

# write a python programa to remove duplicates from list

def list_entr():
    n = int(input('enter max len of the list'))
    list = [int(input('enter elems into list:')) for i in range(n)]
    return list

def rm_dup():
    list = list_entr()
    dict = {}
    l = []
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for k,v in dict.items():
        if v == 1:
            l.append(k)

print(rm_dup())

########################################################################

# python program to print the duplicates in a list, not just the duplicates
# but the whole list of elements

def list_entr():
    n = int(input('enter max len of the list:'))
    list = [int(input('enter elems into list')) for i in range(n)]
    return list

def show_dups():
    list = list_entr()
    dict = {}
    l = []
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for k,v in dict.items():
        if v > 1:
            for i in list:
                if k == i:
                    l.append(i)
    return l

print(show_dups())

########################################################################

# check if the list is empty

def list_check(list):
    if len(list) == 0:
        return 'list is empty'

print(list_check([]))

########################################################################

# write a python program to find the list of words that are not longer
# than n from a given list of words

def list_words():
    n = int(input('enter the max len of string:'))
    list = [input('enter the words') for i in range(n)]
    return list

def len_words(n):
    list = list_words()
    l = []
    for i in list:
        if len(i) < n:
            l.append(i)
    return l

print(len_words(int(input('enter the len that needs to be compared:'))))

########################################################################

# write a python program that takes two list and returns true if both
# list contains atleast one common element


n = int(input('enter the max len of list l:'))
m = int(input('enter the max len of list m:'))

l = [int(input('enter elems into list l:')) for i in range(n)]
p = [int(input('enter elems into list m:')) for i in range(m)]


def list_compar():
    '''
    compare elements in
    a list
    '''
    for i in l:
        for j in p:
            if i == j:
                return 'True'

print(list_compar())

########################################################################

# write a program to print the specified list after removing 0,2,4 and 5
# elements

def list_removal(list):
    l = []
    for i in range(len(list)):
        if i not in [0,2,4,5]:
            l.append(list[i])
    return l

print(list_removal([1,2,3,4,5,5,6,7,8]))

########################################################################

# shuffle and print a given list

import random

def list_entr():
    n = int(input('enter max len of list:'))
    list = [int(input('enter elems into list:')) for i in range(n)]
    return list

def shuffle_list():
    list = list_entr()
    l = []
    m = random.sample(range(len(list)), len(list))
    for i in m:
        l.append(list[i])
    return l

print(shuffle_list())

########################################################################

# generate all permutations of a given list


########################################################################

# python program to get the difference between two lists

n = int(input('enter the max len of list l:'))
m = int(input('enter the max len of list p:'))

l = [int(input('enter elems in to list l:')) for i in range(n)]
p = [int(input('enter elems into list p:'))] for i in range(m)]
