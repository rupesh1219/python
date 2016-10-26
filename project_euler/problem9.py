'''
A pythogoream triplet is a set of three natural numbers,
a<b<c for which sq(a)+sq(b) = sq(c)

there exists only one pythogorean triplet for which
a+b+c = 1000. Find the product of abc
'''

'''
1.find the list of all three numbers where sum of all three
numbers is 1000
then find the where it is pythogorean triplet
then find the product of that list
'''

def triplet():
    for c in range(2,1000):
        for a in range(1,c):
            b = 1000 - c -a

            if a**2 + b**2 == c**2:
                return a*b*c

print(triplet())
