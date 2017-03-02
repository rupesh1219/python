'''
write a python program to calculate the sum of a list of
numbers
'''

'''
steps:
1. generate a random list of 10 numers in a given range
2. then sum the list

note: ;this can directly be added as we generate alist but
as  we are practicing data structures we want to generate a
list and then add the numbers in list
'''

import random

l = random.sample(range(100),10)
print(l,len(l))

counter = 0
i = 0

for i in range(len(l)-1):
    counter += l[i]

print(counter)
