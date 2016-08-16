import Account

class SavingAccount(Account):

    deposite_fee = 2

    def deposite(self, amount):
        return Account(self, amount - self.deposite_fee)