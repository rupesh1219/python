########################################################################
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



