class Bank_Account():
    def __init__(self, Owner, balance):
        self.Owner=Owner
        self.balance=balance
    def withdraw(self, amount):
        if(amount>self.balance):
            print(f"Insufficient funds")
            print(f"Available balance: {self.balance}")
        else:
            self.balance-=amount
            print(f"Available balance after withdrawal: {self.balance}")
    def deposit(self, amount):
        self.balance+=amount
        print(f"Available balance after depositing: {self.balance}")
account = Bank_Account("Bhavya.N", 100)
print(f"Account details, Owner:{account.Owner}, available balance:{account.balance}")
account.deposit(100)
account.withdraw(300)
