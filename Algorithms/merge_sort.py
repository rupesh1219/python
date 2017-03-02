'''
Merge Sort:
Divide and Conquer Algorithm
'''

import random

m = int(input('enter the range for the sample:'))
n = int(input('enter the length of the sample list:'))

l = random.sample(range(m),n)

def merge_sort(l):
    print('splitting',l)
    if len(l)>1:
        mid = len(l)/2
        lefthalf = l[:mid]
        righthalf = l[mid:]
        print(lefthalf)
        print(righthalf)

        merge_sort(lefthalf)
        merge_sort(righthalf)
