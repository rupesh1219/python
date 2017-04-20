###############################################################################

# generators, generate an iterable value to find sum of two elemets i zero


def sum_two_zero(lst, target):
    '''
    return a iterable
    genrator
    '''
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == 0:
                result = (lst[i], lst[j])
                yield result

for i in sum_two_zero([1,2,3,-1,-2,6], 0):
    print(i)
