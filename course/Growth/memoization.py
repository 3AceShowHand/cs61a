def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted


