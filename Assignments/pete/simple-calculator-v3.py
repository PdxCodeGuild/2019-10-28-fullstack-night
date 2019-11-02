'''
simple-calculator-v3.py
Allow the user to enter a full arithmetic expression and use eval to evaluate it.
'''
expression = input(
    "Welcome to Simple Calculator v3.  Please enter an arithmetic expression(i.e.: \"2 + 3\" or \"(9 * 7) / (88 - 9)\") and the calculator will evalue it: "
    )
while True:
    try:
        if expression == 'done':
            print(
                "Thanks for using Simple Calculator v3."
                )
            break
        else:
            result = eval(expression)
            expression = input(f"{expression} = {result}\nEnter another expression or type 'done': "
            )
    except:
        expression = input("Please enter a valid arithmetic expression: ")