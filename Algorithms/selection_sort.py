'''
selecton sort:
1. Repeatedly finds the minimum element from the unsorted list and
moves the element to the begining of the list.
2. This algorithm maintains two sublists where one is sorted and the
other is unsorted
'''

from datetime import datetime
import random


m = int(input('enter the length of the range m:'))
n = int(input('enter the length of the list n:'))

l = random.sample(range(m), n)

print(l)

m = []
n = []

starttime = datetime.now()

for i in range(0,len(l)):
    m.append(min(l))
    l.remove(min(l))


print(datetime.now() - starttime)

print('ascending order of the list using selection sort {}'.format(m))

# selectoi sort performed well compared to insertoin sort as I increse the
# size of the list.
