'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
steps:

create two loops so that you can generate product
convert that product into string
check if reverse of a string is same as original
then find the max of the list generated
'''

m = []

def palindrom_func():
    for i in range(100,999):
        for j in range(i+1,999):
            a = i*j
            b = str(a)
            if b[::-1] == b[:len(b)]:
                m.append(a)
    return max(m)

print(palindrom_func())
