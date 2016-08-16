def split(n):
    """
    Split positive n into all but its last digit and its last digit.
    """
    return n // 10, n % 10

def sum_digits(n):
    """
    Return the sum of the digits of positive integer n.
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2* last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def cascade(n):
    if n < 10:
        print (i)
    else:
        print (n)
        cascade(n//10)
        print (n)

def count_partition(n, size):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif size == 0:
        return 0
    else:
        with_m = count_partition(n-size, size)
        without_m = count_partition(n, size-1)
        return with_m +without_m