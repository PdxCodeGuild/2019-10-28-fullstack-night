'''
simple-calculatorv1.py
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.
'''
operations = ['+', '-', '*', '/']
running = True
while running == True:
    operation = input(
        "Welcome to Simple Calculator v1.0\nWhat operation would you like to perform? + - * /: "
        )
    if operation not in operations:
        continue
    else:
        running = False
        break
num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))
if operation == '+':
    result = num1 + num2
if operation == '-':
    result = num1 - num2
if operation == '*':
    result = num1 * num2
if operation == '/':
    result = num1 / num2
print(f"{num1} {operation} {num2} = {result}")
