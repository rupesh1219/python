########################################################################
# initial practice on generators
########################################################################

# normal function dont regain the state of a function
# but generators can yeild at a point and can be regained again


def gen_nums():
    n = 0
    while n < 4:
        yield n
        n += 1

print(gen_nums())

########################################################################
# fibonacci sequence using generators
########################################################################

def fib1(n):
    counter = 0
    while counter <= n-2:
        yield counter

def fib2(n):
    counter = 1
    while counter <= n-1:
        yield counter

def fib(n):
    '''
    adding both the generators
    '''
    fib1 = fib1(n)
    fib2 = fib2(n)
    yield fib1 + fib2

print(fib(20))
print(next(fib(20)))
