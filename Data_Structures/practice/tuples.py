########################################################################

# write a python program to create a tuple

x = tuple()
#convert list to a tuple
l = [1,2,3]
y = tuple(l)

# crate a tuple
nntuplex = 1,3,4
print(tuplex)
# tuple calling
y[0]
y[1]

########################################################################

# create a tuple with different data types

'''
tuples can take different data types
'''

tuplex = 1,'rf',3
print(tuplex)

########################################################################

# create a tuple with numbers and print one item

'''
we are using list representation to the tuples to call them ???'''

tuplex = 1,2,3
print(tuplex[0])

# creating a tuple of one item

tuplex = 1,
print(tuplex)

########################################################################

# write a python program to unpack the tuples into different variables

tuplex = 1,2,3
n1,n2,n3 = tuplex

print(n1,n2,n3)

########################################################################

# write a program to add an element into a tuple

tuple = 1,2,3
b = 4

tuple = tuple + (b,)
print(tuple)

'''
or we can convert tuple into list and then add that item into list and
convert back to tuple
'''
########################################################################

# convert a tuple to a string

def tuple_string(tuple_items):
    string = ''
    for i in tuple_items:
        string += str(i)
    return string

print(tuple_string((1,2,3)))

########################################################################

# write a program to get 4th element and 4th element from last in a tuple

def fourth_tuple(tuple_item):
    if len(tuple_item) >= 4:
        return tuple_item[3],tuple_item[-4]
    else:
        return "tuple's length is not more than 4"

print(fourth_tuple((1,2,3,4,5,6)))

########################################################################

# write a program to find the repeated items in a tuple

def repeated_items(tuple_item):
    list_item = []
    for i in tuple_item:
        if tuple_item.count(i) > 1:
            list_item.append(i)
    tuple_result = tuple(list_item)
    return tuple_result


print(repeated_items((1,2,3,2,3,1,4,5)))

########################################################################

# write a program to check if element exists in a tuple

def element_exist(tuple,n):
    for i in tuple:
        if tuple.count(n) >= 1:
            return 'element exists'
        else:
            return 'element doesnt exists'

print(element_exist((1,2,3),4))

########################################################################

# write a program to convert list into a tuple

def list_tuple(list):
    return tuple(list)

print(list_tuple([1,2,3]))

########################################################################

# write a program to remove an item from tuple

def remove_element(tuple_items, value):
    '''
    tuples are immutable so we
    cannot remove elements from
    tuple
    '''
    list_items = list(tuple_items)
    list_result = list_items.remove(value)
    return tuple(list_result)

print(remove_element((1,2,3), 3))

########################################################################

# write a program to slice a tuple

def slice_tuple(tuple_items):
    if len(tuple_items) % 2 == 0:
        result1 = tuple_items[:int(len(tuple_items)/2)]
        result2 = tuple_items[int(len(tuple_items)/2):]
    else:
        result1 = tuple_items[:int((len(tuple_items)/2 + 1))]
        result2 = tuple_items[(int(len(tuple_items)/2 + 1)):]
    return result1, result2

print(slice_tuple((1,2,3,4,5,6)))

########################################################################

# write a python program to find the index of an item in a tuple

def index_item(tuple, n):
    return tuple.index(n)

print(index_item((1,2,3,4),4))

########################################################################

# convert tuple of tuples to a dictionary

def tuple_dict(tuple):
    '''
    converting tuple of tuples
    to a dictonary
    '''
    dict_result = dict((k,v) for k,v in tuple)
    return dict_result

print(tuple_dict(((1,2),(2,3))))

########################################################################

# unzip a list of tuples in to individual lists

def tuple_list(tuple):
    '''
    unzip list of tuples
    into individual lists
    '''
    for i in tuple:
        print(list(i))

tuple_list(((1,2),(3,4),(6,7)))

########################################################################

# write a program to reverse a tuple

def reverse_tuple(tuple):
    return tuple[::-1]

print(reverse_tuple((1,2,3)))

########################################################################

# write a program to convert list of tuples into a dictionary

def list_tup_dict(list):
    '''
    list of tuples to
    a dictionary
    '''
    dict_result = dict((k,v) for k,v in list)
    return dict_result

print(list_tup_dict([(1,2),(2,3),(3,4)]))

########################################################################

# print a tuple with string formatting

def string_tuple(tuple):
    return 'this is a tuple {}'.format(tuple)

print(string_tuple((1,2,3)))

########################################################################

# write a program to replace a last element is list of tuples

def list_tuples(list_items, replace_element):
    '''
    replace last element
    in list of tuples
    '''
    for i in list_items:
        a = list(i)
        a[-1:] = replace_element
        list_items[i] = tuple(a)
    return list_items

print(list_tuples([(1,2,3), (3,4,5), (5,6,7)], 9))

########################################################################

# count the elements in a tuple until you see a tuple in tuple

def tuple_tuple(tuple_items):
    count = 0
    for i in tuple_items:
        if isinstance(i, tuple) is False:
            count += 1
        else:
            return count

print(tuple_tuple((1,2,3,(4,5),6)))

########################################################################
