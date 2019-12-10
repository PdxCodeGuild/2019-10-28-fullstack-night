
transaction_list = [] # because you're using one list initialized outside of the init function, multiple atms will have conflicting transaction lists

class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = int(balance)
        self.interest_rate = float(interest_rate)
        self.transaction_list = transaction_list

    def current_balance(self):
        return (f"Currnt Balance ${self.balance}") # What is "currnt"!?!?

    def deposit(self, amount):
        self.balance += int(amount)
        self.calc_interest()
        self.transaction_list.append(f"User deposited ${amount}.")

    def check_withdrawl(self, amount):  # this should return a boolean, true or false
        if self.balance >= int(amount):
            return amount

# def is_vowel(in_letter):
#     return in_letter in 'aoeuiy'
# user_letter = input('choose a letter: ') # choose a letter: o
# if is_vowel(user_letter):
#     print('it is a vowel!') # it is a vowel

        # if self.balance < int(amount):
        #     print("Insufficient funds.")

    def withdraw(self, amount):  # this should be something like, "if check_withdrawal returned True, let them withdraw funds"
        self.balance -= int(amount)
        self.transaction_list.append(f"User withdrew ${amount}.")

    def calc_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)

    def print_transactions(self):
        print(transaction_list)  # consider using ',\n'.join(transaction_list) or something

    def __repr__(self):
        return str(self.balance) + "ATM"


money = ATM('0')  # Usually you'd just put in an integer and not convert, but your way is good too
# money.deposit('4')
# money.check_withdrawl('3')
# money.withdraw('3')
# money.current_balance()
# money.calc_interest()

# print(money.transaction_list)
# print(ATM)

actions = ["deposit", "withdraw", "check balance", "history", "quit"]

while True:  # clean repl, but you don't need any of those `continue`s. an `if/elif/else` block in a `while true` loop will just run one indented section and then loop back.
    action = input(f"What ATM command would you like to perform: \nDeposit, Withdraw, Check Balance, History, Quit ").casefold()

    if action not in actions:
        print("Please enter a valid command.")
        continue

    elif action == "quit":
        print("Goodbye.")
        break

    elif action == "check balance":
        print(money.current_balance())
        continue

    elif action == "deposit":
        deposit_amount = int(input("How much do you want to deposit? "))
        money.deposit(deposit_amount)
        print(money.transaction_list)
        continue

    elif action == "withdraw":
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if not money.check_withdrawl(withdraw_amount):
            print("Insufficient funds.")
            continue
        else:
            money.withdraw(withdraw_amount)
            print(money.transaction_list)
            continue

    elif action == "history":
        money.print_transactions()
        continue
