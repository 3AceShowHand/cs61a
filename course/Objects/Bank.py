class Bank:
    """
    A bank has accounts and pays interest
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, account_type = Account):
        account = account_type(holder)
        account.deposite(amount)
        self.accounts.append(account)
        return account

    def pay_intreset(self):
        for account in self.accounts:
            account.deposite(account.interest * account.balance)