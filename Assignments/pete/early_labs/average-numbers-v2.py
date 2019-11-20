'''
average-numbers-v2.py

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)

# Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4
'''
print("Welcome to the Averagizer V.2.\n")
nums = []
running = True
while running == True:
    add_num = (input("Add a number to the list, or type 'done' to finish: "))
    if add_num == 'done':
        running = False
        break
    else:
        nums.append(int(add_num))
        continue
sum_num = sum(nums)
avg_num = sum_num / (len(nums))
print(f"\nThe sum of {len(nums)} numbers is {sum_num} so the average is {avg_num}.\nThe Averagizer V 2.0 Thanks YOU!")