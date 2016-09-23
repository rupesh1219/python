########################################################################
############################LISTS - 1###################################
########################################################################

'''
given a list or array return true if 6 appears as a first element or the
last element in the list
'''

l = []

maxlen = int(input('enter the length of the list:'))

while len(l) < maxlen:
    item = int(input('enter item to the list:'))
    l.append(item)
    print(l)

if l[0] == 6 or l[maxlen-1] == 6:
    print('true')

########################################################################

'''
given an array return true if first and last element of the list are
equal
'''

l = []

maxlen = int(input('enter max length of the list:'))

while len(l) < maxlen:
    item = int(input('enter item to the list:'))
    l.append(item)
    print(l)

if l[0] == l[maxlen-1]:
    print('true')
else:
    print('false')
########################################################################

'''
return an int aray containing first three digits of pi
'''
#importing math module to get pi value

import math

m = []
l = str(math.pi)

for i in range(4):
    if l[i] != '.':
        m.append(l[i])

print(m)
########################################################################

'''
given two array return true if they have same first element or same last
element and min len of these lists is 1
'''

l = []
m = []

maxlenl = int(input('enter max len of list l:'))

maxlenm = int(input('enter max len of list m:'))

while len(l) < maxlenl:
    item = int(input('enter numbers into list l:'))
    l.append(item)
    print(l)

while len(m) < maxlenm:
    item = int(input('enter numbers into list m:'))
    m.append(item)
    print(m)

if l[0] == m[0] or l[maxlenl-1] == m[maxlenm-1]:
    print('true')
else:
    print('false')
########################################################################
'''
given an array of length 3 add all the elements in
the list and provide the sum as output
'''

l = []

while len(l) < 3:
    item = int(input('enter elements into list'))
    l.append(item)
    print(l)

additionres = 0

for i in range(len(l)):
    additionres += l[i]

print(additionres)
########################################################################
'''
given an array of any length  return a new array with
rotate left for example 1,2,3 to 2,3,1
'''

l = []

while len(l) < 6:
    item = int(input('enter the elements into list:'))
    l.append(item)
    print(l)

def rotate_list(l,n):
    return l[n:]+l[:n]

print(rotate_list(l,1))
########################################################################
'''
given an array of any length print that list in reverse order
'''
l = []

maxlenl = int(input('enter the len of  the list:'))

while len(l) < maxlenl:
    item = int(input('enter items into the list:'))
    l.append(item)
    print(l)

print(l[::-1])

########################################################################

'''
compare the last and fitst element of the array and print the complete
list with the largest element
'''

l = []

maxlenl = int(input('enter the len of the list:'))

while len(l) < maxlenl:
    item = int(input('enter items into list:'))
    l.append(item)
    print(l)

if l[0] > l[maxlenl-1]:
    for i in range(maxlenl):
        l[i] = l[0]

else:
    for i in range(maxlenl):
        l[i] = l[maxlenl-1]

print(l)
########################################################################

'''
add first two elements of the list if the len is > =2  and <2 just print
the list  and if len is 0  the print 0
'''

l = []

maxlenl = int(input('enter the len of the list:'))

while len(l) < maxlenl:
    item = int(input('enter items into list:'))
    l.append(item)
    print(l)

if len(l) >= 2:
    print(l[0]+l[1])
elif len(l) == 1:
    print(l)
else:
    print('not a valid length')
########################################################################

'''
given two arrays of length 3 return a new array/list of length 2
containing middle elements of the list/array
'''

l = []
m = []

while len(l) < 3:
    item  = int(input('enter elements into list l:'))
    l.append(item)
    print(l)

while len(m) < 3:
    item  = int(input('enter elements into list m:'))
    m.append(item)
    print(m)

n = []

n.append(l[1])
n.append(m[1])

print('mid elements of both list:', n)
########################################################################
'''
given an array of any length search for some elements in the list and
print true if those elements are present in the list
'''

l = []

maxlenl = int(input('enter max len of list l:'))

for i in range(maxlenl):
    item = int(input('enter elements into list:'))
    l.append(item)
    print(l)
    if l[i] == 2 or l[i] == 3:
        print('true')

########################################################################
###########################LISTS - 2####################################
########################################################################
'''
return the even ints in a given list
'''

l = []

maxlenl = int(input('enter the max len of list l:'))

for i in range(maxlenl):
    item = int(input('enter items in to list L:'))
    l.append(item)
    print(l)

count_even = 0
count_odd  = 0

for i in range(maxlenl):
    if l[i]%2 == 0:
        count_even += 1
    else:
        count_odd += 1

print('count of even numbers are {} and count of odd numbers are  {}'.\
      format(count_even,count_odd))
########################################################################
'''
given an array of length m find the difference between the largest and
smallest elements
'''

l = []

maxlenl = int(input('enter the max len of the list l:'))

#enter elements in to the list using while loop

for i in range(maxlenl):
    item = int(input('enter elements into list l:'))
    l.append(item)
    print(l)

# now find the max and min elements in the given list
# sort the given list from smallest to largest and then subtract the
# first and last index values in the list to get the required result

def max_min():
    '''
    this function prints the list in ascending order it can be reversed
    to create the list in descending order
    '''
    for i in range(maxlenl):
        for j in range(i+1,maxlenl):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    print('ascending oder of list is {} and descending order of list\
is {}'.format(l[:maxlenl],l[::-1]))
    return l[0]+l[maxlenl-1]


print('sum of largest and smallest elements:', max_min())

# an extension to this problem is to form a list with random numbers
# for given length and compute time taken by the problem as the list
# size is increasing

# form a list with random numbers for given length

import random

m = int(input('enter range for selecting random samples m:'))
n = int(input('enter the length of the list to be formed:'))

l = random.sample(range(m),n)

print(l)

def max_min():
    for i in range(n):
        for j in range(i+1,n):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    print('asennding order fof list is {} and descending order of list\
    is {}'.format(l[:n], l[::-1]))
    return l[0]+l[n-1]

print('sum of max and min functions is:', max_min())

########################################################################
'''
centered average: avoid the smallest and largest elements of the list
and find the average of other elements in the list given that if there
are multiple smallest or largest take a copy while averaging
'''

l = []

maxlenl = int(input('enter the max len of the list:'))

for i in range(maxlenl):
    item = int(input('enter elements into list:'))
    l.append(item)
print(l)

def sort_func():
    for i in range(maxlenl):
        for j in range(i+1,maxlenl):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
                print(l)
    print('ascneding order of list {} and descending order of list\
    is {}'.format(l[:maxlenl], l[::-1]))
    return l

print(sort_func())

def avg_func():
    counter = 0
    i = 0
    denominator = 0
    for i in range(i+1,maxlenl-1):
        counter += l[i]
        denominator += 1
    return int(counter/denominator)

print('centered average of a given list on removing smallest and largest\
elements is {}'.format(avg_func()))
########################################################################
'''
in a given list sum up all the elements if the element is >=13 dont
inlcude in the addition
'''

import random

n = int(input('enter max len of list n:'))

l = random.sample(range(20), n)
print(l)

counter = 0

# concept of global variables introduded in the program

def return_sum():
    global counter
    for i in range(n):
        if l[i] < 13:
            counter += l[i]
    return counter

print(return_sum())
########################################################################
'''
in a given list if there is a 6 then which is followed by 7(immediately)
or after some elements then ignore them while summing up
'''

l = []

maxlenl = int(input('enter the max len of the list l:'))

for i in range(maxlenl):
    item = int(input('enter elements into list l:'))
    l.append(item)
    print(l)

m = []

def sum_cond():
    counter = counter1 = counter2 = counter3 = counter4 = 0

    for i in range(maxlenl):
        if l[i] != 6:
            counter += l[i]
            counter1 += i
        else:
            for j in range(i+1,maxlenl):
                counter2 += l[j]
                m.append(l[j])

    for i in m:
        if m[i] == 7:
            counter3 = i
            print(counter3)

            for i in range(counter3+1,counter1-):
                counter4 += m[i]
        else:
            counter4 += m[i]
            print(counter4)

    for i in range(counter3+1, maxlenl):
        counter4 += l[i]

    return counter + counter4

print(sum_cond())
print(m)
########################################################################

'''
given an array return true if the array contains 2 and has 2 follwing
somwhere in the list
'''
l = []

maxlenl = int(input('enter the maxlen of the list l:'))

for i in range(maxlenl):
    item = int(input('enter elements into list l:'))
    l.append(item)
    print(l)

for i in l:
    if l[i] == 2:
        counter = i
        break

conter = ''
for j in range(i+1,maxlenl):
    if l[j] == 2:
        conter = 'true'
        print(conter)

if conter != 'true':
    print('false')
########################################################################
