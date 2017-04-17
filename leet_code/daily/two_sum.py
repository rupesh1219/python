###############################################################################
# given an array of integers, return indices of two numbers such that they add
# up to given target
# [2,3,5,6] target = 11
# return (2,3)
###############################################################################


def two_sum(lst, target):
    '''
    returns the indices of
    numbers that add up to target
    '''
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)

print(two_sum([3,4,45,3], 7))
