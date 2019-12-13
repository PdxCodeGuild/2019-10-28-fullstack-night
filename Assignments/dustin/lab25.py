'''
By: Dustin DeShane
Filename: lab25.py
'''

class ATM:
    def __init__(self, balance=0, interest_rate=.001, history_list=[]):
        self.balance = balance  
        self.interest_rate = interest_rate
        self.history_list = history_list

    def check_balance(self):
        print(self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        self.history_list.append(f"User deposited ${amount}.")

    def check_withdrawal(self, amount):
        if self.balance-amount >= 0:
            return True

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.history_list.append(f"User withdrew ${amount}.")
        else:
            print("Insufficient funds!")

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        print(f"You have collected ${interest} in interest!")
            
    def history(self):
         self.history_list = []

standing_there = True

my_atm = ATM()

while standing_there:
    menu_choice = input("Please choose one of the following options:\nCheck Balance, Deposit, Withdraw, Interest Earned, or Quit\n")
    selection = menu_choice.lower()
    


    if selection == "check balance":
        my_atm.check_balance()
    elif selection == "deposit":
        amount = float(input("How much would you like to deposit?: "))
        my_atm.deposit(amount)
    elif selection == "withdraw":
        amount = float(input("How much would you like to withdraw?: "))
        my_atm.withdraw(amount)
    elif selection == "interest earned":
        my_atm.calc_interest()
    elif selection == "quit":
        print("Thank you! Goodbye!")
        standing_there = False
        break
    else:
        print("Please try again enter a valid option.")

print(my_atm.history_list)

        
