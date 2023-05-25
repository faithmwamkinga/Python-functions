class Account():
    bank_name="Equity"
    def __init__(self,name,balance,account_number):
        self.balance=balance
        self.name=name
        self.account_number=account_number
        self.deposit=[]
        self.withdrawal=[]
        self.loan_balance=0
    def check_balance(self):
        return f"Your balance is {self.balance}"
    def deposits(self,deposit_transaction):
        deposit_transaction={
            "amount":2000,
            "narration":"deposit"
        }
        new=self.deposit.append(deposit_transaction)
        print(f"The amount deposited is {new}")
    def withdrawals(self,withdrawal_transaction):
        withdrawal_transaction={
            "amount":3000,
            "narration":"withdrawal"
        }
        new_amount=self.withdrawal.append(withdrawal_transaction)
        print(f"The amount is now {new_amount}")
    def print_statement():
         deposit_transaction={
            "amount":2000,
            "narration":"deposit"
        }
         withdrawal_transaction={
            "amount":3000,
            "narration":"withdrawal"
        }
         
         list=[]
         list.append(withdrawal_transaction)
         list.append(deposit_transaction)
         for i in list:
            print(f"You deposited {deposit_transaction} and withdrew {withdrawal_transaction}")
             
    # def count_money(self,amount):
    #     print(f"The amount is {amount}")
    # def withdraw(self,amount):
    #     if self.balance <= amount:
    #         print(f"{self.balance} is not enough")
    #     else:
    #        self.balance-=amount
    #        print(f"{self.balance}")
