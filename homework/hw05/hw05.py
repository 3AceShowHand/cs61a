##############################################################
# An alternative implementation of the tree data abstraction #
##############################################################

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return {'<root>': root, '<branches>': branches}


def root(tree):
    return tree['<root>']


def branches(tree):
    return tree['<branches>']


def is_tree(tree):
    if type(tree) != dict or '<root>' not in tree or '<branches>' not in tree:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)


###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])


def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])


def sides(m):
    """Select the sides of a mobile."""
    return branches(m)


def left(m):
    """return the left sub mobile."""
    return end(sides(m)[0])


def right(m):
    """return the right sub mobile."""
    return end(sides(m)[1])


def torque(s):
    """return the torque of a side."""
    return length(s) * size(end(s))


def length(s):
    """Select the length of a side."""
    return root(s)


def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]


def weight(size):
    """Construct a weight of some size.
    weight是一个没有子树的最小树。
    """
    assert size > 0
    return tree(size)


def size(w):
    """Select the size of a weight.
    如果是一个weight值，那么就没有branches，直接返回以其为root的值。
    """
    return root(w)


def is_weight(w):
    """Whether w is a weight, not a mobile.
    如果是叶子节点，那么就是一个weight值。
    """
    return is_leaf(w)


def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])


def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, u, v = examples()
    >>> print_tree(t)
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(t))
    3
      1
        2
      2
        1
    >>> print_tree(t)  # t should not change
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(v))
    9
      4
        3
          1
            2
          2
            1
      2
        6
          5
            1
          1
            5
              2
                3
              3
                2
    >>> print_tree(v)  # v should not change
    None
      4
        None
          1
            2
          2
            1
      2
        None
          5
            1
          1
            None
              2
                3
              3
                2
    """
    "*** YOUR CODE HERE ***"
    # 判断当前节点是不是个根节点，如果是那么None，求和。如果不是，则有值在其中，直接返回该值。
    total = total_weight(m) if root(m) is None else root(m)
    return tree(total, [side(length(s), with_totals(end(s))) for s in sides(m)])


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    m = with_totals(m)
    # 如果是叶子节点，返回真
    if is_weight(m):
        return True
    # 如果全平衡，那么当前平衡，且左平衡和右平衡。
    balance = torque(sides(m)[0]) == torque(sides(m)[1])
    return balance and balanced(left(m)) and balanced(right(m))


############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    pds = []

    def with_draw(amount, pd):
        nonlocal pds
        nonlocal balance
        if len(pds) == 3:
            return "Your account is locked. Attempts: " + str(pds)
        elif amount <= balance and pd == password:
            balance -= amount
            return balance
        elif pd != password:
            pds.append(pd)
            return "Incorrect password"
        elif amount > balance:
            return "Insufficient funds"

    return with_draw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'
    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10
    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    draw = withdraw(0, old_password)
    if type(draw) == str:
        return draw

    def joint(amount, attempt):
        if attempt == old_password or attempt == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, attempt)

    return joint


###########
# Objects #
###########

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, describe, price):
        self.describe = describe
        self.price = price
        self.counts = 0
        self.current_balance = 0

    def vend(self):
        if self.counts == 0:
            return "Machine is out of stock."
        if self.current_balance < self.price:
            return "You must deposit ${0} more.".format(self.price - self.current_balance)
        elif self.current_balance == self.price:
            self.current_balance = 0
            self.counts -= 1
            return "Here is your {0}.".format(self.describe)
        else:
            change = self.current_balance - self.price
            self.current_balance = 0
            self.counts -= 1
            return "Here is your {0} and ${1} change.".format(self.describe, change)

    def restock(self, count):
        self.counts = count
        return "Current {0} stock: {1}".format(self.describe, self.counts)

    def deposit(self, current_balance):
        self.current_balance += current_balance
        if self.counts == 0:
            return "Machine is out of stock. Here is your ${0}.".format(self.current_balance)
        return "Current balance: ${0}".format(self.current_balance)


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    "*** YOUR CODE HERE ***"

#############
# Challenge #
#############
