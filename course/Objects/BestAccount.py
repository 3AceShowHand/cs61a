import CheckingAccount

class BestAccount(CheckingAccount, SavingAccount):

    def __init__(self, account_holder):
        CheckingAccount.__init__(self, account_holder)
        self.balance = 1 