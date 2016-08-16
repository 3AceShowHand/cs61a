class Bear:
    """Go bears."""

    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'
        
    def __str__(self):
        return 'some bear'

    def __repr__(self):
        return 'Bear()'

def repr(x):
    return type(x).__repr__(x)



oski = Bear()
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())