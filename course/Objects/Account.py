__auther__ = "Jinl"

class Account:
    interst = 0.02
    
    def __init__(self, holder, balance = 0):
        self.holder = holder
        self.balance = balance

    def deposite(self, n):
        self.balance += n
        return self.balance

    def withdraw(self, n):
        if self.balance < n:
            print("Insuffient Account")
        self.balance -= n
        return self.balance



# if __name__ == "__main__":
#     tom_account = Account('Tom')
#     tom_account.deposite(300)
#     tom_account.withdraw(130)
#     tom_account.deposite(200)
#     tom_account.withdraw(250)
#     # Looking up an attribute name in an object may return:
#     # one of its isinstance attribute or one of the attributes of its class.
#     getattr(tom_account, 'balance')
#     hasattr(tom_account, 'withdraw')
