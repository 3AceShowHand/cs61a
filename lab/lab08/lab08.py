# Q3
def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_count = 0
    def make_counter():
        count = 0
        def counter(msg):
            nonlocal global_count, count
            if msg == "count":
                count += 1
                return count
            elif msg == "reset":
                count = 0
            elif msg == "global-count":
                global_count += 1
                return global_count
            elif msg == "global-reset":
                global_count = 0
        return counter
    return make_counter


# Q4
def intersection(xs, ys):
    """
    >>> a = Link(1)
    >>> intersection(a, Link.empty) is Link.empty
    True

    >>> b = a
    >>> intersection(a, b).first # intersection begins at a
    1

    >>> looks_like_a = Link(1)
    >>> intersection(a, looks_like_a) is Link.empty # no intersection! (identity vs value)
    True

    >>> b = Link(1, Link(2, Link(3, a)))
    >>> a.first = 5
    >>> intersection(a, b).first # intersection begins at a
    5

    >>> c = Link(3, b)
    >>> intersection(b, c).first # intersection begins at b
    1
    >>> intersection(c, b).first # intersection begins at b
    1

    >>> intersection(a, c).first # intersection begins at a
    5
    """
    if xs is Link.empty or ys is Link.empty:
        return Link.empty
    if len(xs) < len(ys):
        return intersection(xs, ys.rest)
    elif len(xs) > len(ys):
        return intersection(xs.rest, ys)

    while xs is not ys:
        xs, ys = xs.rest, ys.rest
    return xs


# Q5
def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    "*** YOUR CODE HERE ***"

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while m < len(first) and n < len(second) and not equal_prefix():
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1
    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


# Q6
def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n*n:
        while b <= n*n:
            sum += (a*b)
            b += 1
        b = 0
        a += 1
    return sum


# Link Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

