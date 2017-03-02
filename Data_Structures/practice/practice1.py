#write a python program to print a string in specific format


print('\nTwinkle, twinkle, little star,\n\t\tHow i wonder what you are!\n\t\t\tUp above the world and so high')

########################################################################

#write a python program to get the python version you are running


import os
os.system('python -V')

########################################################################

#write a python program to display current date and time

'''
we have various modules in python like datetime
through which we can get and modify date times.
'''
import datetime

now = datetime.datetime.now()
print(now)

print(now.hour)
print(now.year)
print(now.month)
print(now.day)

########################################################################

#compute the area of a circle on accepting the radius
#of a circle from user

'''
get the value of pi from import math
make sure you inlcude user input as float
'''
import math

#r = float(input('enter the radius of circle:'))

def area_of_circle(r):
    area = math.pi*(r**2)
    print(area)

area_of_circle(float(input('enter the radius of circle:')))

########################################################################

# write a python progaram which accepts the user firstname
# and last name to print them in reverse with a space
# between them

def output_name(f,l):
    print("{}{}{}".format(l,' ',f))

output_name(input('enter firstname:e'),input('enter lastname'))

########################################################################

# write a python program to return list and tuple of numbers
# when a user input of comma separated sequence is given

for i in range(10):
    l = int(input('enter sequence of numbers')).partiton(',')

# wirte a program to accept the filename from user and
# print the extension of the filename

def print_ext(file_name):
    for i in range(len(file_name)):
        if file_name[i] == '.':
            print(file_name[i+1:])
            break

print_ext(file_name=input('enter a filename with extesnsion:'))

########################################################################

# write a program to take a list and print the first and last elements

color_list = ['red', 'black', 'brown', 'orange']

print(color_list[0])
print(color_list[len(color_list)-1])

########################################################################

# write a program to display the examinaton schedule from
# exam_st_date=(11,12,2016) as 11/12/2016

'''
given a tuple with three elements print data format using
the tuple  data
'''

def tuple_play(tup):
    s = ''
    print(len(tup))
    for i in tup:
        if i == int(len(tup)-1):
            s += str(i)
        else:
            s += str(i) + '/'
    return s

print(tuple_play((11,12,2016)))

########################################################################

# write a python program that accepts an integer n and computes
# n+nn+nnn

def print_docs(func):
    return help(func)

print(print_docs(input('enter the function for which you need:')))

########################################################################

import calendar

y = int(input('enter the year:'))
m = int(input('enter the month:'))
print(calendar.month(y,m))

########################################################################

# calculate number of dates between two dates in a calendar


########################################################################

# calculate the volume of sphere for given radus

import math

def vol_sphere(r):
    vol = 4/3*math.pi*(r**3)
    return vol

print(vol_sphere(int(input('enter the radius value:'))))

########################################################################

# write a program to get the difference between a numner and 17, if the
# number is greater than 17 double the absolute difference

def abs_diff(n):
    if n<17 :
        return abs(n-17)
    else:
        return 2*(n-17)

print(abs_diff(int(input('enter a number:'))))

########################################################################

# write a program to find whether the number is within 100 of 1000 or
# 2000

def within(n):
    if (n > 900 and n < 1000) or (n >1900 and n < 2100):
        print('number is within the range: %d',n)
    else:
        print('number is out of range')

within(int(input('enter a number:')))

########################################################################

# write a program to find the sum of three numbers, if three numbers
# are equal then pinrt the sum as thrice the value

def thrice_sum(m,n,o):
    if m==n==o:
        return 3*(m+n+o)
    else:
        return m+n+o

print(thrice_sum(3,3,4))
print(thrice_sum(4,4,4))

########################################################################

# write a program to return is + string if "is" is not present in the
# string, if its present just return the string

def is_string(s):
    if len(s) > 2 and s[:2] == 'Is':
        return s
    return 'Is' + s

print(is_string(input('enter a string:')))

########################################################################

# write a python program to get a new string which is n copies of given
# string.

def n_copies(s,n):
    return n*s

print(n_copies(input('enter a string:'), int(input('enter n int value:'))))

########################################################################

# write a program to find whether the given number is even or odd and
# print out the appropriate message to user

def ev_od_num(n):
    if n % 2 == 0:
        return 'its an even number'
    return 'its an odd number'

print(ev_od_num(int(input('enter a number:'))))

########################################################################

# write a function to count the number 4 in a given list

n = int(input('enter the length of list:'))
m = int(input('enter the number that you want to count:'))

def list_input(n):
    l = []
    for i in range(n):
        l.append(int(input('enter a number in to list:')))
    return l

def count_num(n,m):
    count = 0
    l = list_input(n)
    print(l)
    for i in range(len(l)):
        if l[i] == m:
            count += 1
    return count


print(count_num(n,m))

########################################################################

# write a program to get n copies of the first 2 characters of a string
# retrun n copies of whole string if length is less than 2

n = int(input('enter how many copies you want:'))
s = input('enter a string:')

def n_copies(n,s):
    if len(s) < 2:
        return n*s
    return n*s[:2]

print(n_copies(n,s))

########################################################################

# write a program to verify the given alphabet is vowel or not

s = input('enter the alphabet:')

def vowel(s):
    l = ['a','e','i','o','u']
    for i in l:
        if s == i:
            return 'vowel'
    return 'not a vowel'

print(vowel(s))

########################################################################

# write a python program to verify if a number exists in the list(

n = int(input('enter a number to find:'))
m = int(input('enter the max range of the list:'))

def iter_list(m):
    l = []
    for i in range(m):
        l.append(int(input('enter the list:')))
    return l


def find_func(n, m):
    l = iter_list(m)
    for i in l:
        if l[i] == n:
            return 'True'
        return 'false'

print(find_func(n,m))

########################################################################

# write a program to create histogram from given list of integers

n = int(input('enter the max range of list:'))

def list_enter(n):
    l = []
    for i in range(n):
        l.append(int(input('enter a number to list:')))
    return l

def histogram():
    l = list_enter(n)
    for i in l:
        print(i * '*')

print(histogram())


########################################################################

# write a program to print the odd value digits in a list

n = int(input('enter the max list range of list:'))

def iter_list(n):
    l = []
    for i in range(n):
        l.append(int(input('enter the list:')))
    return l

def even_odd_values():
    l = iter_list(n)
    m = []
    o = []
    for i in range(len(l)):
        if i%2 != 0:
            m.append(l[i])
        else:
            o.append(l[i])
    return o, m

print(even_odd_values())

########################################################################

# write a program to concatenate all elements in a list into a string
# and return it

n = int(input('enter the max range of list:'))

def iter_list(n):
    l = []
    for i in range(n):
        l.append(input('enter values into list:'))
    return l

def concatenate_elem():
    l = iter_list(n)
    s = ''
    for i in l:
        s += i
    return s

print(concatenate_elem())

########################################################################

# given a string print the elements into a list(

s = input('enter a string:')

def num_list(s):
    l = []
    for i in range(len(s)):
        l.append(int(s[i]))
    return l

print(num_list(s))

########################################################################

# compare sets and print the elements that are not present in set2
# when compared with set1

set1 = set(['white','back','red'])
set2 = set(['red','green'])

list1 = list(set1)
list2 = list(set2)

print(len(list1))
print(len(list2))

def func_comp(list1, list2):
    l = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                l.append(l[i])
    return set(l)

print(func_comp(list1, list2))

########################################################################

# write a program to accept the base and height of a triangle to calculate
# the area of triangle

b = float(input('enter the base of a triangle:'))
h = float(input('enter the height of a traingle:'))

def triangle(b,h):
    area = 1/2*b*h
    return area

print(triangle(b,h))

########################################################################

# calculate the GCD of two integers

########################################################################

# calculate the LCM of two integers

#######################################################################

# write a program to print the sum of 3 integers, if both the numbers
# are equal print zero

def list_iter():
    l = []
    for i in range(3):
        l.append(int(input('enter the elements in to list:')))
    return l

def sum_elem():
    l = list_iter()
    for i in range(len(l)):
        for j in (i, len(l)):
            if l[i] == l[j]:
                return 0
            else:
                return

########################################################################

# write a program to return sum of two intergers if the sum is between
# 15 and 20 return 20

def sum_int(n,m):
    if m+n >=15 and m+n<=20:
        return 20
    return m+n

print(sum_int(int(input('enter n:')),int(input('enter m:'))))

########################################################################

# write a program to return true if two intergers are equal or if sum or
# difference is equal to 5

n = int(input('enter a number n:'))
m = int(input('enter a number m:'))

def return_true(m,n):
    if m == n or abs(m-n) == 5 or m+n == 5:
        return True
    return False

print(return_true(m,n))

########################################################################

# write a program to add two objects if they are of integer type

l = [1,2]
m = ['rup',3]

def add_twoint(l):
    if type(l[0]) == int and type(l[1]) == int:
        return l[0] + l[1]

print(add_twoint(l))

########################################################################

# write a program to display your details like name, age, address
# in different lines

n = int(input('enter the max range of list:'))

def take_input(n):
    l = []
    for i in range(n):
        l.append(input('enter elements in to string:'))
    return l

def print_values():
    l = take_input(n)
    for i in l:
        print(i)

print_values()

########################################################################

# write a program to solve (x+y) * (x+y)

x = int(input('enter number x:'))
y = int(input('enter number y:'))

def product_xy(x,y):
    product = (x+y)**2
    return product

print(product_xy(x,y))

########################################################################

# write a program to check whether a file exists or not
'''
1. add all files to a list from the directory
2. search for a file in the given list
'''

import os

list = os.listdir()

def list_file(list):
    print(list)
    for i in list:
        if i[:2] == 'pr':
            return 'file exists'

print(list_file(list))

########################################################################

# write a program to get OS, platoform and release date

import platform
import os

print(os.name)
print(platform.system())
print(platform.release())

########################################################################

# print how many cpu are running on your machine

import multiprocessing

print(multiprocessing.cpu_count())

########################################################################

# print the filename that is currenlty executing

import os
print('current filename is:',os.path.realpath(__file__))

########################################################################

n = input('input a string that needs to be formatted:')

def formatting():
    for i in range(len(n)):
        if n[i] == '.':
            return float(n)
        return int(n)

print(formatting())

########################################################################

# write a python program to print without new line or space

for i in range(10):
    print('*')

for i in range(10):
    print('*', end= '')

########################################################################

# get profile status of a program
# know the time taken by various parts of the program

import cProfile

def sun():
    addition = 0
    for i in range(10):
        addition += i
    print(addition)
cProfile.run('sun()')

########################################################################

# write a program to print to stderr

def sun():
    sys.stderr.write('there is an err')

sun()

########################################################################

# access environment variables using python
import os

print(os.environ)
print(os.environ['HOME'])

########################################################################

# get the username of the system
# getpass acutally reads the environmental varaibles to get the names
import getpass
print(getpass.getuser())

########################################################################

# write a program to get the execution time of python method

import time

def func_iter():
    start_time = time.time()
    l = []
    for i in range(100):
        if i%7 == 0:
            l.append(i)
    end_time = time.time()
    return (l,end_time-start_time)

print(func_iter())

'''
why return in a function return values in a tuple format by default
'''

########################################################################

# write a program to find the sum of first n postive intergers

n = int(input('enter the value n:'))

def sum_n():
    sumn = 0
    for i in range(n+1):
        sumn += i
    return sumn

print(sum_n())

########################################################################

# write a program to convert height(ft and inch) in to cm

n = (input('enter a string of height:'))

def htocm():
    return (int(n[0])*12*2.54) + (int(n[2])*2.54)

print(htocm())

########################################################################

# write a program to get the absolute filepath of a file

import os

print(os.path.realpath('practice1.py'))

########################################################################

# write a python program to return the file creation and modified dates

import time,os.path

print(time.ctime(os.path.getctime('practice1.py')))
print(time.ctime(os.path.getmtime('practice1.py')))

########################################################################

# write a program to sum the digits in a integer

n = int(input('enter the number:'))

def int_sum():
    m = str(n)
    sumn = 0
    for i in m:
        sumn += int(i)
    return sumn

print(int_sum())

########################################################################

import os.path,time

def tim_fil():
    l = os.listdir('.')
    print(l)
    for i in l:
        print(time.ctime(os.path.getctime(i)))

tim_fil()

########################################################################

# get the details of math function
def ret_math():
    print(help('math'))

ret_math()

########################################################################

# write a program to hash a word

import hashlib

hash_obj = hashlib.sha1(b'hello rupesh')
hex_digit = hash_object.hexdigest()
print(hex_digit)

########################################################################

# get the copyright information

import sys

print(sys.copyright)

########################################################################
