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
    #def deposits(self,deposit_transaction):
     #   deposit_transaction={
      #      "amount":2000,
       #     "narration":"deposit"
        #}
        #self.deposit.append(deposit_transaction)
        #print(f"The amount deposited is {self.deposit}")
    def deposit(self,amount):
        self.balance+=amount
        transaction={"amount":amount,"narration":"deposit"}
        return transaction
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
def borrow_loan(self,amount):
           if self.loan_balance > 0:
              return f"There is an outstanding balance of {self.loan_balance}"
           elif amount<100:
             return "loan limit must not exceed 100"
           elif len(self.deposit)<100:
            return f"the number "
           total_deposits=sum([transaction["amount"]for transaction in self.deposits])
           limit =total_deposits/3
           if amount<=limit:
                   self.loan_balance+=amount
                   print ("Loan successfuly borrowed ")
           elif amount>limit:
                   print ("Loan borrowed exceeds limit")
           else:
             print("Loan does not meet requirements")

def repay_loan(self,amount):
    if amount> self.loan_balance:
        diff =amount-self.balance
    return f""
def transfer(self,amount,account):
    if amount<=self.balance:
        account.deposit(amount)
        self.balance-=amount
    else:
        return f"Insufficient balance"
    # def count_money(self,amount):
    #     print(f"The amount is {amount}")
    # def withdraw(self,amount):
    #     if self.balance <= amount:
    #         print(f"{self.balance} is not enough")
    #     else:
    #        self.balance-=amount
    #        print(f"{self.balance}")
