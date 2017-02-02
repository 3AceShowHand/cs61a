class Bear:
    """A Bear."""

    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'A Bear'

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    return repr(x)

if __name__ == '__main__':
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__str__())
    print(oski.__repr__())