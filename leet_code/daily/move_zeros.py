###############################################################################
# given a list move all zeros to the end of the list
# dont change the order of elements in list
# dont use extra data structures
# try to minimize your operations
###############################################################################

def count_zeros(lst):
    '''
    returns count of
    zeros in list
    '''
    count = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count += 1
    return count


def move_zeros(lst):
    '''
    move zeros to the
    end of the list
    '''
    count1 = count_zeros(lst)
    print(count1)
    for i in range(count1):
        for j in range(len(lst)-1):
            if lst[j] == 0:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

print(move_zeros([1,2,3,0,5,0,0,8,7,0]))
