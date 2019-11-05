# Handle ^C on the keyboard and print a nice message!
try:
  while True:
    operand = input("Enter your operand (+, -, *, /): ")
    first_number = float(input("Enter your first number: "))
    second_number = float(input("Enter your second number: "))

    if operand == "+":
      result = first_number + second_number
      print(f"{first_number} + {second_number} = {result}")
    elif operand == "-":
      result = first_number - second_number
      print(f"{first_number} - {second_number} = {result}")
    elif operand == "*":
      result = first_number * second_number
      print(f"{first_number} * {second_number} = {result}")
    elif operand == "/":
      result = first_number / second_number
      print(f"{first_number} / {second_number} = {result}")
except KeyboardInterrupt:
  print("\nThanks for using the calculator!")