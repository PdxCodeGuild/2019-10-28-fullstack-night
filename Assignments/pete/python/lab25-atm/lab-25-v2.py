'''
Version 2

Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.
'''
class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions_list = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions_list.append(f"User deposited ${amount}")
        return self.balance

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions_list.append(f"User withdrew ${amount}")
        return self.balance

    def calc_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return interest, self.balance

    def print_transactions(self):
        for transaction in self.transactions_list:
            print(transaction)

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
atm_test.print_transactions()