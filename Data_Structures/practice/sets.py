########################################################################
# learning sets in python
########################################################################

# write a python program to iterate over sets

def iterate_sets(set_item):
    '''
    iterate over a set
    '''
    for i in set_item:
        print(i)


print(iterate_sets({1,2,3,4}))

########################################################################

# write a program to add item to a sets

def update_set(set_item):
    '''
    add an element to set
    '''
    set_item.add(4)
    return set_item

print(update_set({1,2,3}))

########################################################################

# remove an element from set

def remove_set(set_item, removal):
    '''
    remove an element from set
    '''
    set_item.discard(removal)
    return set_item

print(remove_set({1,2,3}, 3))

########################################################################
