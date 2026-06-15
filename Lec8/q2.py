# Create Accoount class with 2 attribute - balance & account no.
# Create Methods for debit , credit & printing the balance.

class Account():
    def __init__(self , acc_no , balance):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self , debit_amt):
        self.balance -= debit_amt
        print("Debited : " , debit_amt , "Remaining Balance is : " , self.balance)

    def credit(self , credit_amt):
        self.balance += credit_amt
        print("Credited : " , credit_amt, "Remaining Balance : ", self.balance)


acc1 = Account("Acc_1" , 10000)
acc1.debit(500)
acc1.credit(1000)