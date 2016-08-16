import Account

class CheckingAccout(Account):
    """
    A bank account that earns less interest and 
    charges for withdraws
    """

    interest = 0.01  # override
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)