'''
sort a list using insertion sort algorithm and compute time for a huge list
generate the list randomly using random module
'''



from datetime import datetime
import random

starttime = datetime.now()

n = int(input('enter the maxlenl if the list l:'))
m  = int(input('enter the range for list l:'))

l = random.sample(range(m),n)
print(l)

for i in range(1,n+1):
    for j in range(i-1,0,-1):
        if l[j] < l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp

print(datetime.now()-starttime)

print('asceding order of the list {} and descending order of the \
list is {}'.format(l[:n],l[::-1]))

print(datetime.now()-starttime)
