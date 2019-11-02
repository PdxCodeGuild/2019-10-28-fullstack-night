#numbers entered by user
num = int(input("How many numbers would you like to enter? "))
#allow a total sum
total_sum = 0

#loop the range in numbers and allows the user to select how many numbers they would like to enter

for n in range (num):
    numbers = float(input("Enter number: "))

#adds the total of numbers entered to the total sum of the set of numbers

    total_sum += numbers

#then divides the total sum to the number of numbers entered

avg = total_sum / num

print ("average of", num, "numbers is:", avg)
