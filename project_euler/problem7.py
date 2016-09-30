'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# generate list of prime numbers until the index of the list is 10000


def is_prime(n):

    for j in range(2,int(n**1/2)+1):
        if n % j == 0:
            return False;
    return True;
