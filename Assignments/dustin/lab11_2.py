oper = input("What type of operation would you like(+, -, * , /)?: ")
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))


expression = str(x) + oper + str(y)

print(expression)
answer = eval(expression)
print(answer)