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


atm_test = ATM(20, .01)
print(atm_test.check_balance())
print(atm_test.balance)
print(atm_test.deposit(850))
print(atm_test.balance)
print(atm_test.check_withdrawal(20))
print(atm_test.withdraw(100))
print(atm_test.balance)
print(atm_test.calc_interest())