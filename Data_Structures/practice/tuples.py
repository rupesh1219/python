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

def remove_element(tuple):

