'''
lab20-credit-card-validation-v1.py

Lab 20: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
'''
credit_card_number = 4556737586899855
def credit_card_validator(credit_card_number):
# Convert the input string into a list of ints
    credit_card_list = list(str(credit_card_number))
    credit_card_int_list = []
    for digit in credit_card_list:
        credit_card_int_list.append(int(digit))
# Slice off the last digit. That is the check digit.
    check_digit = credit_card_int_list[15]
# Reverse the digits.
    reversed_list = credit_card_int_list[::-1].pop()
# Double every other element in the reversed list.
    false = True
    double_every_other_list = []
    for digit in reversed_list:
        if false == False:
            false = True
            double_every_other_list.append(digit)
        else:
            double_every_other_list.append(digit * 2)
            false = False
# Subtract nine from numbers over nine.
    minus_nines_list = []
    for digit in double_every_other_list:
        if digit > 9:
            minus_nines_list.append(digit - 9)
        else:
            minus_nines_list.append(digit)
# Sum all values.
    list_sum = sum(minus_nines_list)
# Take the second digit of that sum.
    sum_string = str(list_sum)
    second_digit_string = sum_string[1]
    second_digit = int(second_digit_string)
# If that matches the check digit, the whole card number is valid.
    if second_digit == check_digit:
        return True
    else:
        return False

print(credit_card_validator(credit_card_number))