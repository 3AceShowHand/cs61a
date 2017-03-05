from operator import add, mul, truediv

def apply_twitce(f, x):
    return f(f(x))

def square(x):
    return x * x

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def reduce(f, s, initial):
    """
    Combine elements of s using f start from initial."""
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    for x in s:
        initial = f(initial, x)
    return initial


def recursive_reduce(f, s, initial):
    >>> recursive_reduce(mul, [2, 4, 8], 1)
    64
    >>> recursive_reduce(add, [1, 2, 3, 4], 0)
    10
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))


def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('int')


