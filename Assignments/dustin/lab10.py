'''
By: Dustin DeShane
Filename: lab10.py
'''

my_sum = 0
count = 0
running = True

while running:
    user_in = input("Enter a number or type 'done': ")
    if str(user_in) == "done":
        running = False
        break
    user_add = float(user_in)
    my_sum = my_sum + user_add
    count += 1

average = my_sum/count

print(f"The average of the numbers you entered is: {average}")
