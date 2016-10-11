'''
Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
'''

def fibonacci_series():
    m = []
    for i in range(1, 4000000):
        if i > 2:
            m.append(m[i-2]+m[i-3])
            if m[i-1] > 4000000:
                break
        else:
            m.append(i)

    print(m[:len(m)-1])

    count = 0
    for i in range(len(m)):
        if m[i]%2 == 0:
            count += m[i]
    print(count)

fibonacci_series()