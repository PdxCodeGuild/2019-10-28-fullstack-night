"""
Name: DJ Thomas
Lab: 11 version 2
Filename: lab11-v1.py
Date: 10-31-2019

Lab covers the following:
    - input()
    - float()
    - if
    - elif
    - while
    - True
    - False
    - Break

"""
#print('Your Calculator! Please choose + , - , / , * or when finished type done.\n') # this print gives guidance on which functions they can use prior to utulizing the calculator.
# I used the 'while True' prior to the code letting all arguments know the word 'done' in variable user_operation is the stop running cue.
#running = True # variable 'running' defines True
#while running: # have to add 'while' followed by the variable 'running' representing True.

user_operation = input('Which operation would you like to use? Or done to exit: ')
user_num_1 = float(input('Pick your fisrt number: '))
user_num_2 = float(input('Pick your second number: '))
finished = done
while finished in user_operation == 'done':
    break


if user_operation == '+': # start with 'if' followed by the user input variable. == means in this line, + its true and run the print.
    print(f'{user_num_1 + user_num_2}') # 'f' number 1 + number 2 creates the output if true.

elif user_operation == '-':
    print(f'{user_num_1 - user_num_2}')
elif user_operation == '/':
    print(f'{user_num_1 / user_num_2}')
elif user_operation == '*':
    print(f'{user_num_1 * user_num_2}')
elif user_operation == 'done':
    break
