'''
Lab 25: ATM

Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

    check_balance() returns the account balance

    deposit(amount) deposits the given amount in the account

    check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative

    withdraw(amount) withdraws the amount from the account and returns it

    calc_interest() returns the amount of interest calculated on the account

'''
class ATM:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return self.balance


atm_test = ATM(500, .02)
print(atm_test.check_balance())
print(atm_test.balance)
print(atm_test.deposit(25))
print(atm_test.balance)
print(atm_test.check_withdrawal(1000))
print(atm_test.check_withdrawal(250))
print(atm_test.withdraw(250))
print(atm_test.balance)
print(atm_test.calc_interest())