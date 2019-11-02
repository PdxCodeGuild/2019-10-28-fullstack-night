"""
Name: DJ Thomas
Lab: 11 version 1
Filename: lab10-v1.py
Date: 10-31-2019

Lab covers the following:
    - input()
    - float()
    - for/in loop
    - fstring
    - range

"""



num = int(input("how many numbers?: "))
total_sum = 0
for i in range(num):
    numbers = float(input('Enter number: '))
    total_sum += numbers
avg = total_sum/num
print(f"Average of {num} numbers is {avg}")
