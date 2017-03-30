########################################################################
# conditional statements with python
########################################################################

# write a python program to create a histogram

def star_histogram(n):
    '''
    create star pattern
    histogram
    '''
    for i in range(1, n+1, 1):
        print(i * '*')

    for i in range(n-1, 0, -1):
        print(i * '*')

print(star_histogram(5))

########################################################################

# write a python program that accepts a word from user and reverses it

def reverse_word(word):
    '''
    reverese a word
    '''
    return word[::-1]

print(reverse_word(input('enter a word to reverse:')))

########################################################################

# python program to count the even and odd numbers from a given sequence

def count_num(tuple_item):
    '''
    count of even and odd
    numbers
    '''
    count_even = count_odd = 0
    for i in tuple_item:
        if i%2 == 0:
            count_even += 1
        else:
            count_odd +=1
    return count_odd, count_even

print(count_num((1,2,3,4,5,6)))

########################################################################

# given a list of elements type its correspoding type

def ele_type(list_items):
    '''
    type of each element
    in a list
    '''
    for i in list_items:
        print(type(i))

print(ele_type([1,2.4,1+3j,(1,2),'rupesh',{'a':1,'b':3}]))

########################################################################

# print a number 1 to 6 expect 3 and 6

def skip_elements(list_items):
    '''
    skip elements and
    print a list
    '''
    for i in list_items:
        if i == 3 or i == 6:
            continue
        print(i)

skip_elements([1,2,3,4,5,6])

########################################################################

# generate fibonacci sequence between 0 and 50








