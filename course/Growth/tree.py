class Tree:
    def __init(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr(self):
        if self.branches:
            branches_repr = ", " + repr(self.branches)
        else:
            branches_repr = ""
        return 'Tree({0}{1})'.format(self.entry, branches_repr)


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.entry + right.entry, [left, right])


def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)


def is_int(x):
    return int(x) == x


def is_odd(n):
    return n % 2 == 1


def hailstone_tree(k, n=1):
    """Return a Tree in which the paths from the leaves to the 
    root are all possible hailston sequences of length k ending in n."""
    if k == 1:
        return Tree(n)
    else:
        branches = []
        branches.append(hailstone_tree(k-1, n * 2))
        less = (n-1) / 3
        if less > 1 and is_int(less) and is_odd(less):
            branches.append(hailstone_tree(k-1, int(less)))
        return Tree(n, branches)


def leaves(t):
    if not t.branches:
        return [t.entry]
    else:
        return sum([leaves(b) for b in t.branches], [])


def longest_path_blow(k, t):
    """return a path all items less than k"""
    if t.entry >= k:
        return []
    elif not t.branches:
        return [t.entry]
    else:
        paths = [longest_path_blow(k, b) for b in t.branches]
        return [t.entry] + max(paths, key=len)