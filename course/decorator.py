def square(x):
    return x ** 2

def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

def trace(fn):
    """
    return a version of fn that first print before it is called.
    """
    def traced(x):
        print ('Calling', fn, 'on argument', x)
        return fn(x)
    return traced
