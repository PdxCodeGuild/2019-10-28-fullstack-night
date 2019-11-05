'''
By: Dustin DeShane
Filename: lab11.py
'''

def add_stuff(x, y):
    return x + y
def subtract_stuff(x, y):
    return x - y
def multiply_stuff(x, y):
    return x * y
def divide_stuff(x, y):
    return x / y


running = True
while running:
    oper = input("What type of operation would you like(+, -, * , /)?: ")
    if oper == "done":
        running = False
        break
    x = float(input("Please enter your first number: "))
    y = float(input("Please enter your second number: "))
    
    #function selection
    if oper == "+":
        answer = add_stuff(x, y)
    elif oper == "-":
        answer = subtract_stuff(x, y)
    elif oper == "*":
        answer = multiply_stuff(x, y)
    elif oper == "/":
        answer = divide_stuff(x, y)
    else:
        answer = "Please try again and use one of the listed operators."
    print(f"The answer is: {answer}")
    print("To exit, please type 'done'.")