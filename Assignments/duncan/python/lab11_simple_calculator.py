
game_in_session = "yes"

while game_in_session == "yes":
    user_operator = input("What is the operation you'd like to perform? ")
    if user_operator == "+":
        first_num = int(input("What is the first number? "))
        second_num = int(input("What is the second number? "))
        print(f"{first_num} + {second_num} = {(first_num) + (second_num)}")
        game_in_session = input("Would you like to perform another operation? ").lower()
    elif user_operator == "-":
        first_num = int(input("What is the first number? "))
        second_num = int(input("What is the second number? "))
        print(f"{first_num} - {second_num} = {(first_num) - (second_num)}")
        game_in_session = input("Would you like to perform another operation? ").lower()
    elif user_operator == "*":
        first_num = int(input("What is the first number? "))
        second_num = int(input("What is the second number? "))
        print(f"{first_num} * {second_num} = {(first_num) * (second_num)}")
        game_in_session = input("Would you like to perform another operation? ").lower()
    elif user_operator == "/":
        first_num = int(input("What is the first number? "))
        second_num = int(input("What is the second number? "))
        print(f"{first_num} / {second_num} = {(first_num) / (second_num)}")
        game_in_session = input("Would you like to perform another operation? ").lower()
    else:
        print("Error!")
else:
    print("Goodbye!")

### Version 3 ###

game_in_session = "yes"

while game_in_session == "yes":
    user_formula = input("What is your formula? ")
    print(f"{user_formula} = {(eval(user_formula))}")
    game_in_session = input("Would you like to perform another operation? ").lower()
else:
    print("Goodbye!")
