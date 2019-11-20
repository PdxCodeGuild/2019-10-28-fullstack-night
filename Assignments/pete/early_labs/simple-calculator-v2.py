'''
simple-calculatorv2.py
Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.
'''
operations = ['+', '-', '*', '/']
operation = input(
    "Welcome to Simple Calculator v2.0\nWhat operation would you like to perform? (+ - * /): "
)
first_run = True
while True:
    if first_run == False:
        operation = input(
            "\nWhat operation would you like to perform? (+ - * /):\nOr type 'done' if finished: "
        )
    if operation == 'done':
        break
    elif operation not in operations:
        first_run = False
        continue
    else:
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
        first_run = False
        continue
