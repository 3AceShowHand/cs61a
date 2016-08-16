from math import gcd

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __repr(self):
        return 'Ratio({0},{1})'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio)
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return self.numer / self.denom + other 
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__

    def __rsub__(self, other):
        return Ratio(-self.numer, self.denom) + other