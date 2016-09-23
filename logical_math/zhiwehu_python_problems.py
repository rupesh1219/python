'''
write a program to find all such numbers which are divisible by 7 but
are not a multiple of 5 and are between 2000 and 3000(both included)
Numbers obtained should be printed in a comma separated sequence in a
single line
'''


for i in range(1999,3000):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end = ",")

#storing the output in a list
#arguments are passed instead of hardcoding the values

l=[]

def fun_divmul(x,y):
    for i in range(1999,3000):
        if i % x == 0 and i % y !=0:
            l.append(i)

fun_divmul(7,5)

print(l)

########################################################################

'''
calculate the factorial of given numbers and store the output in a list
or output to console in a comma separate sequence
'''

'''
steps to be taken:
1. create an empty list and pass the numbers for which you want to'
calculate the factorial into a list
2. iterate the list and store the factorials in a list
3. output the list to console
'''

t = []
m = [2,3,4]

for j in m:
    fact = 1
    for i in range(1, j+1):
        fact *= i
    t.append(fact)
print(t)

########################################################################
'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

l={}
j = int(input('enter a value for the list to calculate the square'))

for i in range(1,j+1):
    sqr = i: i*i
    l.append(sqr)
print(l)

# how to output this into a dictionary
