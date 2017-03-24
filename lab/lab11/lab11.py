#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.current = start
        self.end = end
        self.start = start

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        self.current = self.start
        return self

# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    def __init__(self, s):
        self.str = s
        self.current = 0
        self.end = len(self.str)

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        result = self.str[self.current]
        self.current += 1
        return result

    def __iter__(self):
        return self

##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
        yield n
        n -= 1


class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, start):
        self.start = start
        self.end = 0
        self.current = self.start
        

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

    def __iter__(self):
        self.current = self.start
        return self


# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n
