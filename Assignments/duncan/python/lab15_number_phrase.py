user_number = int(input("Enter your number: "))
tens_digit = user_number//10
ones_digit = user_number%10

ones_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens_list = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
mixed_list = ["", "eleven", "twelve", "thirteen", "", "fifteen", "", "",  "eighteen", "teen"]

tens_phrase = ""
ones_phrase = ""
mixed_phrase = ""

while True:
    if tens_digit and ones_digit == 1:
        mixed_phrase = mixed_list[tens_digit]
        print(f"Your number: {mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 2:
        mixed_phrase = mixed_list[ones_digit]
        print(f"Your number: {mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 3:
        mixed_phrase = mixed_list[ones_digit]
        print(f"Your number: {mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 4:
        mixed_phrase = mixed_list[9]
        print(f"Your number: {ones_list[ones_digit]}{mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 5:
        mixed_phrase = mixed_list[ones_digit]
        print(f"Your number: {mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 6:
        mixed_phrase = mixed_list[9]
        print(f"Your number: {ones_list[ones_digit]}{mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 7:
        mixed_phrase = mixed_list[9]
        print(f"Your number: {ones_list[ones_digit]}{mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 8:
        mixed_phrase = mixed_list[ones_digit]
        print(f"Your number: {mixed_phrase}.")
    elif tens_digit == 1 and ones_digit == 9:
        mixed_phrase = mixed_list[9]
        print(f"Your number: {ones_list[ones_digit]}{mixed_phrase}.")

    if tens_digit < 1:
        tens_phrase = tens_list[0]
    elif tens_digit == 1:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 2:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 3:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 4:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 5:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 6:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 7:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 8:
        tens_phrase = tens_list[tens_digit]
    elif tens_digit == 9:
        tens_phrase = tens_list[tens_digit]

    if ones_digit < 1:
        ones_phrase = ones_list[0]
    elif ones_digit == 1:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 2:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 3:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 4:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 5:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 6:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 7:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 8:
        ones_phrase = ones_list[ones_digit]
    elif ones_digit == 9:
        ones_phrase = ones_list[ones_digit]
    break

print(f"Your number: {tens_phrase}{ones_phrase}.")

# print(f"Number: {tens_digit}{ones_digit}.")


### Instructor Solution ###

tens_words = {
0: '',
2: 'twenty',
3: 'thirty',
4: 'fourty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety',
}
ones_words = {
0: '',
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',

}
def two_digit_number_to_phrase(number):
    tens = number // 10
    ones = number % 10
    if number < 13:
        return ones_words[number]
    elif number >= 13 and number < 20:
        if number == 15:
            return 'fifteen'
        else:
            return ones_words[ones]+'teen'
    elif number >= 20:
        return f"{tens_words[tens]}-{ones_words[number]}".strip("-") # prints the numbers defined below following the operations defined above
        # .strip removes any trailing "-"

def three_digit_number_to_phrase(number):
        if number < 100:
            return two_digit_number_to_phrase(number)
        elif number >= 100:
            hundreds = number // 100
            return f"{ones_words[hundreds]} hundred {two_digit_number_to_phrase(number % 100)}"

assert two_digit_number_to_phrase(5) = "five" #assert will fail if the comparison given is Not True
assert two_digit_number_to_phrase(12) = "twelve"
assert two_digit_number_to_phrase(15) = "fifteen"
assert two_digit_number_to_phrase(30) = "thirty"
assert two_digit_number_to_phrase(55) = "fifty-five"
