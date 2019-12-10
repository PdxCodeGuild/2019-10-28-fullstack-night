'''
Version 3

Allow the user to enter commands into a REPL.
'''
class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions_list = []

    def check_balance(self):
        print(f"Your balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions_list.append(f"User deposited ${amount}")
        print(f"You deposited ${amount}")
        return self.balance

    def check_withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        else:  # you don't need else here. don't worry about two `return`s running
            return True
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions_list.append(f"User withdrew ${amount}")
        print(f"You withdrew ${amount}")
        return self.balance

    def calc_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return interest, self.balance

    def print_transactions(self):
        for transaction in self.transactions_list:
            print(transaction)  # consider something like ",\n".join(transaction_list)

repl_atm = ATM()
print("Welcome to the ATM.")
while True:  # clean repl, nice!
    command = input("What would you like to do do?\n(deposit, withdrawal, check balance, transaction history, or exit): ").casefold()
    if command == 'deposit':
        deposit_amount = int(input("How much would you like to deposit? $"))
        repl_atm.deposit(deposit_amount)
    elif command == 'withdrawal':
        withdrawal_amount = int(input("How much would you like to withdraw? $"))
        sufficient_funds = repl_atm.check_withdrawal(withdrawal_amount)
        if sufficient_funds == True:  # You don't need the == True
            repl_atm.withdraw(withdrawal_amount)
    elif command == 'check balance':
        repl_atm.check_balance()
    elif command == 'transaction history':
        repl_atm.print_transactions()
    elif command == 'exit':
        break
    else:
        print("Please enter a valid command")
print("Thanks for using the ATM")


'''
looks great! if you want to reorganize your code in a fun way, you can make a dictionary that has methods as values.

>>> option_dict = {'a': lambda: print('a'), 'b': lambda: print('b' + input('punctuation: '))}
>>> user_input = input('a or b: ')
a or b: b
>>> option_dict.get(user_input, lambda: print('not a or b'))
<function <lambda> at 0x7f99cfe3a440>
>>> option_dict.get(user_input, lambda: print('not a or b'))()
punctuation: !
b!
>>> option_dict.get(input('a or b: '), lambda: print('not a or b'))()
a or b: c
not a or b
>>> 

'''
