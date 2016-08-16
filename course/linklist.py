class linklist:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is linklist.empty or isinstance(rest, linklist)
        self.first = first
        self.rest = rest

    # element selection []
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        
