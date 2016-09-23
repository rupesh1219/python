'''
practice strings in python

here are some of the coding bat python string problems
'''
########################################################################

'''
given a string name "rupesh"
return a greeting of the form "hello rupesh!"
'''

#input the name in console and pass the name to function

name = str(input("enter a name:"))

def greet_name(name):
    return "hello" + " " + name + "!"

print(greet_name(name))

# define a function to greet a person

def greet_name(name):
    return "hello" + name + "!"

print(greet_name('rupesh'))

########################################################################
'''
given a string a and b, return the result putting them together in the
order abba
'''

#pass two arguments using console to a function

str1 = str(input("enter string1:"))
str2 = str(input("enter string2:"))

def str_fun(str1,str2):
    return str1 + str2 + str2 + str1

print(str_fun(str1,str2))

# chatting with computer using python prgramming language

str1 = str(input("HI! how are you? Can you please enter your name?"))

def greet_name1(str1):
    return "Hi" + str1 + "!"

print(greet_name1(str1))

########################################################################

'''
given an 'out' string length 4 such as <<>> and a word, return a new
string that looks like "<<word>>"
'''

str1 = str(input("enter the special character string:"))
str2 = str(input("enter the word:"))

def concat_fun(str1,str2):
    return str1[:2] + str2 + str1[2:4]

print(concat_fun(str1,str2))

########################################################################
'''
given a string return a new string made of 3 copies of the last 2 chars
of the original string, length will be atleast 2
'''
'''
difference between comparision and assigning
a==2:comparision
a=2: assigning
'''


str1 = str(input("enter a string to do the operation:"))
int1 = int(len(str1))

print(int1)


def fun_operation(str1):
    if int1>2:
        return 3*str1[int1-2:int1]
    if int1==2:
        return 3*str1[:2]
    else:
        print("not sufficient length to do the operation")

print(fun_operation(str1))

########################################################################

'''
given a string of even length return first half of the string if the
string is not even return invalid entry
'''

str1 = str(input('enter a string:'))
int1 = int(len(str1))
print(int1)

def half_fun(str1):
    '''doc strings:
    an example for how python 3 behaves for divisons which gives folat
    numbers so used int of that number below as string indices accepts
    only integers
    '''
    if int1 % 2 == 0:
        return str1[:int(int1/2)]
    else:
        return 'invalid length'

print(half_fun(str1))

########################################################################

'''
given two strings return a string of the form short+long+short based on
lengths
'''

str1 = str(input('enter string1:'))
str2 = str(input('enter string2:'))
int1 = int(len(str1))
int2 = int(len(str2))


def short_long(str1,str2):
    if int1>int2:
        return str2 + str1 + str2
    if int1<int2:
        return str1 + str2 + str1
    else:
        return 'invalid length for the function'

print(short_long(str1,str2))

########################################################################

'''
given a string return 'rotated left 2' version where first two characters
go to the left and the last characters come to the front
'''

str1 = str(input('enter a string to pass as a argument to function:'))

def left2(str1):
    if len(str1)>=2:
        return str1[2:len(str1)] + str1[:2]
    else:
        return 'invalid length'

print(left2(str1))

########################################################################
######################## STRINGS 2 ####################################
########################################################################

'''
given a string , return a string where for every char in the original
there are two characters
interesting argument in print statement learnt during this:
1. by default in python print in for loop takes \n but inorder to
have your output in single straight line "end" argument in python
is very useful which overwrites the default \n
'''

str1 = str(input('enter a string:'))

def double_char(str1):
    for i in str1:
        print (i+i,end="")

double_char(str1)

########################################################################

'''
count a word in a given string,for example in "abvhi hi hi" there are 3
hi's in the string.
'''
'''
problem flow:
1. for each index in string find out that first match is 'h' and consecutive
index is 'i' then count that word and go on
'''

str1 = str(input('enter a string:'))

def count_hi(str1):
    num_count = 0
    for i in range(len(str1)-1):
        if str1[i:i+2]=='hi':
            num_count += 1
    return num_count
print(count_hi(str1))

########################################################################

'''
return true if the string 'cat' and 'dog' appear the same number of times
in the given string
'''

str1 = str(input('enter a string:'))

def cat_dog(str1):
    num_count = 0
    num_count1 = 0
    for i in range(len(str1)-1):
        if str1[i:i+3] == 'cat':
            num_count += 1
        if str1[i:i+3] == 'dog':
            num_count1 += 1
    print(num_count)
    print(num_count1)

    if num_count == num_count1:
        print('true')

cat_dog(str1)

'''
research more on search algorithms and extend it to text search
'''
########################################################################

'''
return the number of times that the string 'code' appears anywhere in
the given string, accept any letter in the place of 'd' such as cooe
or cope count as code
'''

str1 = str(input('enter a string:'))

def count_code(str1):
    count = 0
    for i in range(len(str1)-1):
        if str1[i:i+2]=='co' and str1[i+2] >= 'a' and str1[i+2] <= 'z' \
           and str1[i+3] == 'e':
            count += 1
    print(count)

count_code(str1)

########################################################################
'''
if either of the strings contain the matched string at the very end of
the other string not case sensitive return true
for example:

hiabc abc return true
not   prinNOt return true
ink  pint return false
'''

str1 = str(input('enter a string:'))
str2 = str(input('enter a string:'))


i = int(len(str1))
j = int(len(str2))

def count_match(str1, str2):
    if len(str1) > len(str2):
        n = len(str2)
        if str1[i-n:] == str2[:j]:
            print('true')
        else:
            print('false')
    if len(str1) < len(str2):
        n = len(str1)
        if str2[j-n:] == str1[:i]:
            print('true')
        else:
            print('false')

count_match(str1, str2)

########################################################################
'''
In a give a string serach for xyz if present return true but if . is
present infront of xyz or if string not prsenet return false
'''

str1 = str(input('enter a string:'))

def count_xyz(str1):
    for i in range(len(str1)-1):
        if str1[i:i+3] == 'xyz':
            if i > 1:
                if str1[i-1] == '.':
                    print('false')
            print('true')

count_xyz(str1)

########################################################################
