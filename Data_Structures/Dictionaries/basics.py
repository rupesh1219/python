########################################################################
############## Basics of dictinory data structure ######################
########################################################################

'''
from learn hard way of python
'''

# create mapping of state abbreviation

states = {
    'Oregon': 'OR',
    'North Carolina': 'NC',
    'New York': 'NY',
    'Texas': 'TX'
}

# create a basic set of states and some cities in them

cities = {
    'NY': 'Brooklyn',
    'NC': 'Charlotte',
    'TX': 'Houston'
}
n
#add some more cities

cities['OR'] = 'Portland'

# print out some cities

print('cities in newyork are:',cities['NY'])

# print some states

print('abbreviation for states are:',states['Oregon'])

# playing with both states and cities data structures

print('city in the state of north carolina',cities[states['North Carolina']])

# more in dictionaries
# iterate through dictionaries

for k,v in states.items():
    print(k,v)
