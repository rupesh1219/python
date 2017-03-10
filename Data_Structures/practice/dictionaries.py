1########################################################################
# PRACTICE OF DICTIONARIES
########################################################################

# write a program to sort the  dictionary by its value

def histogram(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def sort_dict():
    dict = histogram(list)
    for v in range(len(dict.values())):
        if v > v+1:
            temp = dict.values[v]
            dict.values[v+1] = dict.values[v]
            dict.values[v] = temp
    return dict.items()

print(histogram([1,2,2,3,3,3,4,4,4]))
print(sort_dict())

'''
if __name__ == '__main__':
    dict = histogram([1,2,2,3,3,3,3,4,4,4])
    print(sort_dict(dict))
'''

########################################################################

# write a python function to add a key to dictionary

def add_dict(dict,key):
    dict[key] = 34
    return dict

print(add_dict({1:3, 3:4},6))

########################################################################

# concatenate the following dictionaries

def concat_dict(dict1, dict2):
    concat_dict = {}
    for d in [dict1, dict2]:
        concat_dict.update(d)
    return concat_dict

print(concat_dict({1:3}, {2:3}))

########################################################################

# write a function to check if key already exists in dictionary

def exists_key(dict1,key):
    for k in dict1.keys():
        print(k)
        if k == key:
            return 'key exists'
        else:
            return 'key doesnt exists'

print(exists_key({1:3,3:4},4))

########################################################################

# write a program to iterate over dictionaries

def iterate_dict(dict):
    for k,v in dict.items():
        print(k,v)
    for k in  dict.keys():
        print(k)
    for v in dict.values():
        print(v)

iterate_dict({1:2,2:3})

########################################################################

# write a program to generate dictionary where value is the square of
# key for a given range


def square_dict(n):
    dict = {}
    for i in range(1,n+1):
        dict[i] = i*i
    return dict
print(square_dict(5))

########################################################################

# write a python program to sum all items in a dictionary

def sum_allitems(dict):
    result = 0
    for k,v in dict.items():
        result += k+v
    return result

print(sum_allitems({1:3,2:4}))

########################################################################

# write a program to multiply all items in a given dictionary

def mul_items(dict):
    prod = 1
    for k,v in dict.items():
        prod *= (k*v)
    return prod

print(mul_items({1:3,3:3}))

########################################################################

# write a program to remove a key from dictionary

def remove_key(dict,k):
    dict.pop(k)
    return dict

print(remove_key({1:2,3:4},3))

########################################################################

# write a python program to map two lists into a dictionary

def map_list(list1, list2):
    dict = {}
    for i,j in zip(list1, list2):
        dict[i] = j
    return dict

print(map_list([1,2], [3,4]))

########################################################################

# write a program to sort a dictionary by key

def sort_dict(dict):
    list_tuples = sorted(dict.items())
    dict2 = {}
    for k in list_tuples:
        for j in k:
            dict2[j] = j+1
    return dict2

print(sort_dict({1:2,3:3,2:3}))

########################################################################

# write a program to get the max and min value in a dictionary

def max_min_value(dict):
    max = 0
    min = 99999
    for v in dict.values():
        if v > max:
            max = v
        if v < min:
            min = v
    return max,min

print(max_min_value({1:2,2:3,4:4}))

########################################################################

# write a program to remove duplicates in a dictionary

def remove_dup(dict):
    '''
    as dictionaries cannot have
    duplicate keys and that means
    identify duplicates in values
    '''
    dict1 = {}
    for k,v in dict.items():
        if v not in dict1.values():
            dict1[k] = v
    return dict1

print(remove_dup({1:3,2:3,3:2,23:6}))

########################################################################

# check to see if dictionary is empty or not

def empty_dict(dict):
    if bool(dict) == False:
        return 'dictionary is empty'
    else:
        return 'dictinoary is not empty'

print(empty_dict({}))

########################################################################

# adding values for  common keys in dictioanries

def adding_dict(dict1, dict2):
    dict3 = {}
    for k1,v1 in dict1.items():
        for k2,v2 in dict2.items():
            if k1 == k2:
                dict3[k1] = v1+v2
            else:
                dict3[k1] = v1
                dict3[k2] = v2
    return dict3

print(adding_dict({1:3,2:4,4:5}, {1:3,2:5,5:4}))

########################################################################

# print all unique values in a dictionary

def unique_values(dict1):
    '''
    print unique values
    '''
    list = []
    for k,v in dict1.items():
        if v not in list:
            list.append(v)
    return list

print(unique_values({1:3,2:3,3:4,5:6}))

########################################################################

# write a program to create nested ditionary of keys from a list

def nested_dict(list):
    '''
    list to nested dict keys
    '''
    dict = {}
    for i in list:
        dict[i] = dict[i+1]
    return dict

print(nested_dict([1,2,3]))

########################################################################

# write a python program to print the dictionary line by line


def dict_line(dict):
    for k,v in dict.items():
        print(k,v)

dict_line({1:3,3:2})

########################################################################
