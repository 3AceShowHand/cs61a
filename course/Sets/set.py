
class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches


class BinaryTree(Tree):
    empty = Tree(None)
    empty.is_empty = True


    def __init__(self, entry, left=empty, right=empty):
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False


    @property
    def left(self):
        return self.branches[0]


    @property
    def right(self):
        return self.branches[1]


    def contain(self, v):
        if self.is_empty:
            return False
        elif self.entry == v:
            return True
        elif self.entry < v:
            return self.right.contain(v)
        else:
            return self.left.contain(v)


    def adjoin(self, v):
        if self.contain(v):
            return self
        else:
            if self.is_empty:
                return Tree(v)
            elif self.entry < v:
                return BinaryTree(self.entry, self.left, self.right.adjoin(v))
            elif self.entry > v:
                return BinaryTree(self.entry, self.left.adjoin(v), self.right)
