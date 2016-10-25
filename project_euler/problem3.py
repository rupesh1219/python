'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

'''
algorithm:
1. find the factors of sqrt of given number.
2. within an inner loop find whether the obtained factor is prime or not
'''


n = int(input('enter the number to find the largest prime factor of it:'))

m = []

#define a number is prime or not


def is_prime(l):
    for k in range(2,int(l**1/2+1)):
        if l%k == 0:
            return False
    return True

for i in range(3,n):
    if n%i == 0:
        if is_prime(i):
            m.append(i)

print(m[len(m)-1])

