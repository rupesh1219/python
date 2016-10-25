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
