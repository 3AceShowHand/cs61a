def gcd(m, n):
    """Return the largest k that evenly divides both m & n
    k, m, n are positive
    >>> gcd(12, 8)
    4
    >>> gcd(7, 7)
    7
    >>> gcd(16, 8)
    8
    >>> gcd (7, 5)
    1
    >>> gcd(2, 16)
    2
    """
    if m == n:
        return n
    elif m < n:
        return gcd (n, m)
    else:
        return gcd (m-n, n)

def curry2(f):
    """
    from operator import add
    add_two = curry2(add)(2)
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def trace1(fn):
    """
    This is a sample of decorator, which is used to decorate function.
    """
    def traced(x):
        print("Calling", fn, 'on argument ', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x ** 2

def sum_square(x, y):
    return square(x) + square(y)

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse = horse(2)
horse(mask)
