'''
By: Dustin DeShane
Filename: lab20.py
'''

keys_to_the_kingdom = "4556737586899855" #input("Please enter your 16-digit credit card number: ")
keys_int = []
for i in keys_to_the_kingdom:
    keys_int.append(int(i)) #convert string to list of ints
print(keys_int)
check_digit = keys_int[15] #set aside final digit to use for validity check
keys_int.pop(15) #remove last digit
print(keys_int)
keys_int.reverse() #reverse list
print(keys_int)
for i, val in enumerate(keys_int): #multiply even digits by 2
    if i % 2 == 0:
        val = val * 2
        keys_int.pop(i) #remove old value from list
        keys_int.insert(i, val) #add new value at the same place(Use replace?)
for i, val in enumerate(keys_int): #subtract 9 from value if >9
    if val > 9:
        val -= 9
    keys_int.pop(i)
    keys_int.insert(i, val)
my_sum = sum(keys_int)
print(keys_int)
print(my_sum)
if my_sum % 10 == check_digit: #check if card number valid
    print("Righteous, dude.")