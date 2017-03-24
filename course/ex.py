def is_prime(n):
    """
    Return true if n is prime number else False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(100)
    False
    >>> is_prime(13)
    True
    """
    if n < 2:
        return False
    elif n % 2 == 0:
        if n == 2:
            return True
        return False
    mid = n // 2
    for i in range(1, mid):
        if n % (2 * i + 1) == 0:
            return False
    return True

def next_prime(n):
    """
    Return next smallest prime bigger than n
    >>> next_prime(2)
    3
    >>> next_prime(3)
    5
    >>> next_prime(11)
    13
    """
    next = n + 1
    while not is_prime(next):
        next = next + 1
    return next

def hogtimus_prime(n):
    """
    return next larger prime number if n is a prime number
    else, return n
    >>> hogtimus_prime(2)
    3
    >>> hogtimus_prime(4)
    4
    >>> hogtimus_prime(1)
    1
    """
    if is_prime(n):
        return next_prime(n)
    return n

def split(n):
    """
    Split positive n into all but its last digit and its last digit.
    """
    return n // 10, n % 10

def is_swap(score):
    """Returns whether the SCORE contains only one unique digit, such as 22.
    """
    # BEGIN PROBLEM 4
    if score < 10:
        return True
    high, low = split(score)
    return high == low
    # END PROBLEM 4

def swine_swap(score, opponent_score):
    """
    swap score if current score only contains unique digit.
    """
    if is_swap(score):
        score, opponent_score = opponent_score, score
        return score, opponent_score
