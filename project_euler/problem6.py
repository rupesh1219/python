'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''


def sum_sqaures():
    j = 0
    for i in range(101):
        j += i**2
    return j

def sum_tosquare():
    j = 0
    for i in range(101):
        j += i
    return j**2

diff = abs(sum_sqaures() - sum_tosquare())

print('difference between sum of squares and square of sum {}'.format(diff))
