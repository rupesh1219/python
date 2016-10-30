'''
sum of primes below 10 are 2+3+5+7 = 17
find sum of primes below 2 million
'''


def is_prime(n):
    for i in range(2,int(n**1/2)+1):
        if n%i == 0:
            return False
    return True


sum  = 2
for i in range(3,2000000,2):
    if is_prime(i):
        sum += i

print(sum)
