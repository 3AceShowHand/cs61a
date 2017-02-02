class Ratio:
    def __init__(self, n, d):
        self.gcd = gcd(n, d)
        self._numer = n // self.gcd
        self._denom = d // self.gcd

    @property
    def numer(self):
        return  self._numer * self.gcd

    @property
    def denom(self):
        return self._denom * self.gcd

    @numer.setter
    def numer(self, value):
        assert value % self._numer == 0
        self.gcd = value // self._numer

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self._numer, self._denom)

    def __str__(self):
        return '{0} / {1}'.format(self._numer, self._denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self._numer + self._denom * other
            d = self._denom
        elif isinstance(other, Ratio):
            n = self._numer * other._denom + self._denom * other._numer
            d = self._denom * other._denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d //g)
    __radd__ = __add__

    def __float__(self):
        return self._numer / self._denom


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n


if __name__ == "__main__":
    print(Ratio(1, 3) + Ratio(1, 6))
    print(1 + Ratio(1, 3))
    print(Ratio(1, 3) + 1)
