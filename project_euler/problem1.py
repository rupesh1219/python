'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_null():
    count = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            count += i
    print('sum of all multiples of 3 or 5 below 1000 {}'.format(count))

sum_null()

'''
using list comprehension
'''

list = [i for i in range(1000) if i%3==0 or i%5==0]
print(sum(list))

'''
using generator

In the above example its not worth creating a list in the memory
as we are trying to find the sum.

How do we avoid not creating a list and find the sum?
'''

print(sum(i for i in range(1000) if i%3 == 0 or i%5 ==0))

def is_divisible_by_any(numerator,denominators):
     for denominator in denominators:
        if numerator % denominator == 0:
            return True
        return False

def sum_divisible(max_range,denominators):
    return sum(
        i for i in range(max_range)
        if is_divisible_by_any(i,denominators)
    )

print(sum_divisible(1000,[3,5]))
