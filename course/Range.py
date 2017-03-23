class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0, self.end - self.start)

    def __getitem__(self, k):
        if k < 0:
            k = len(self) + k
        if k < 0 or k >= len(self):
            raise IndexError
        return self.start + k

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start, self.end)


class RangeIter:
    def __init__(self, start, end):
        self.next = start
        self.end = end

    def __next__(self):
        if self.next >= self.end:
            raise StopIteration
        result = self.next
        self.next += 1
        return result


class LetterIter:
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end
    
    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration
        result = self.next_letter
        self.next_letter = chr(ord(result)+1)
        return result


class Letters:
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end

    def __iter__(self):
        return letter_generator(self.start, self.end)

    
def letter_generator(next_letter, end):
    while next_letter < end:
        yield next_letter
        next_letter = chr(ord(next_letter)+1)