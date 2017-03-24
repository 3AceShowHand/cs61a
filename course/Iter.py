class IteratorA:
    def __init__(self):
        self.start = 10

    def __next__(self):
        if self.start > 100:
            raise StopIteration
        self.start += 20
        return self.start
    def __iter__(self):
        return self

iterator = IteratorA()
A = [num for num in iterator]
B = [num for num in iterator]
