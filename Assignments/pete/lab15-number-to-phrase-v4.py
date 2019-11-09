'''
lab15-number-to-phrase-v4.py
Version4
Convert a time given in hours and minutes to a phrase.
'''

# print("Welcome to Number to Phrase v4.0.  This program will convert that digital clock reading into an easily-pronounceable phrase to impress friends and family with your clock reading skills!")

#this function splits the input into 3 lists
def clock_to_lists(clock):
    clock = clock.replace(' ', '').replace(':', '')
    clock_list= list(clock)
    if len(clock_list) == 5:
        clock_list.insert(0, '0')

    hour_list = clock_list[0 : 2]
    minute_list = clock_list[2 : 4]
    am_pm_list = clock_list[4 : 6]
    return hour_list, minute_list, am_pm_list

#this function converts hour_list into a text string
def hour_converter(hour_list):
    hour_string = ''.join(hour_list)
    hour_dict = {
        '01': 'one',
        '02': 'two',
        '03': 'three',
        '04': 'four',
        '05': 'five',
        '06': 'six',
        '07': 'seven',
        '08': 'eight',
        '09': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
    }
    hour_text = hour_dict[hour_string]
    return hour_text
#this function gets the minute digits
def minute_digits(minute_list):
    minute_int = int(''.join(minute_list))
    return minute_int

#i pulled all this from the v1 example and changed some variables and deleted unnecessary lines
tens_words = {
    0: '',
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
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
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

#i changed this to fit my code:
def miunte_converter(minute_int):
    tens = minute_int // 10
    ones = minute_int % 10
    if minute_int < 20: 
        minute_text = ones_words[minute_int]
    elif minute_int >= 20:
        minute_text = f"{tens_words[tens]}-{ones_words[ones]}".strip("-")
    return minute_text

def am_pm_converter(am_pm_list):
    am_pm_text = ''.join(am_pm_list)
    return am_pm_text

def the_grand_combiner(hour_text, minute_text, am_pm_text):
    text = f"It's {hour_text} {minute_text} {am_pm_text}."
    return text

 clock = input("Gimme dat time: ")
 

