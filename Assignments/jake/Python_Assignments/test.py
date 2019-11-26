num = int(input("How many numbers would you like to enter? "))
total_sum = 0

for n in range (num):
    numbers = float(input("Enter number: "))

    total_sum += numbers

avg = total_sum / num

print ("average of", num, "numbers is:", avg)
