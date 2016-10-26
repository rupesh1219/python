'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# generate list of prime numbers until the index of the list is 10000

import itertools
# this function says whether a number is prime or not
def is_prime(n):

    for j in range(2,int(n**1/2)+1):
        if n % j == 0:
            return False
    return True

# how to print prime numbers in a given range(


#explored how to generate inifinte loop using itertools
#itertools.count starts with the given argument and can step using
#step argument

def prime_num():
    m = []
    for i in itertools.count(start=2):
        if is_prime(i):
            m.append(i)
            if len(m) == 10001:
                return m[10000]
print(prime_num())
