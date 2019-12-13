'''
By: Dustin DeShane
Filename: lab15.py
'''
#dictionaries for number to string conversion
convert_ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "",}
convert_tens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety", 10: "one hundred"}
convert_special = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

running = True
while running:
    number_to_convert = int(input("Please enter a number between 0 and 100: ")) # consider putting a try/except block here
    if number_to_convert in range(0,100): #checks for range
        running = False
        break
    else:
        print("Please try again.")


if number_to_convert == 0:
    print("zero")
elif number_to_convert > 10 and number_to_convert < 20:
    print(convert_special[number_to_convert])
else:
    ones = number_to_convert % 10
    tens = number_to_convert // 10
    #print(f"{tens} {ones}")
    converted_ones = convert_ones[ones]
    if number_to_convert < 10:
        print(f"{converted_ones}")
    if number_to_convert >= 10:
        converted_tens = convert_tens[tens]
        print(f"{converted_tens} {converted_ones}")
