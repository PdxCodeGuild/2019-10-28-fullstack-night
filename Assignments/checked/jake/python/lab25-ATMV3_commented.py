import math  # You aren't using this import, are you?

# atm lab allowing the user to input and decide what they want to do and how much $$ is in their account
class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: "))  # You probably want to take this in as a parameter, not have the input in the method
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: "))  # You probably want to take this in as a parameter, not have the input in the method
        if self.balance>=amount:   # this should be a separate method that returns a boolean
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  
# code being driven
   
# the object of the class 
s = Bank_Account() 
   
# callable functions with the class
s.deposit()   # This should all be in a repl
s.withdraw() 
s.display() 
