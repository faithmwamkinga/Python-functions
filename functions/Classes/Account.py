class Account():
    bank_name="Equity"
    def __init__(self,name,balance,account_number):
        self.balance=balance
        self.name=name
        self.account_number=account_number
    def count_money(self,amount):
        print(f"The amount is {amount}")
    def withdraw(self,amount):
        if self.balance <= amount:
            print(f"{self.balance} is not enough")
        else:
           self.balance-=amount
           print(f"{self.balance}")
    def deposit(self,amount):
        print(f"The amount deposited is {amount}")