class Products:
    market="Marikiti market"
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.mobile_money="M-pesa"
        self.mobile_banking="KCB"
        self.quantity=quantity
    def total_amount(self):
        total_cost=self.price*self.quantity
        return f"You have bought {self.quantity} {self.name} each at {self.price}, total amount is {total_cost} Kes"
    def select_method(self):
        pay_method=input("Choose payment mode")
        if pay_method=="Mobile Money":
            return self.mobile_money
        elif pay_method=="Mobile Banking":
            return self.mobile_banking
        else:
            return "Buy by credit"
        

# Function to pay money
def payment(self):
        amount = float(input("Enter amount to be paid: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Paid:", amount)
        else:
            print("\n Insufficient balance ")