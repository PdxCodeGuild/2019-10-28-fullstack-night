#prompting user to give a number of ft to be converted to meters practice dictionary
#dictionary== key value pairs

r#####read evaluate print loop
'''
units = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1*1*1,
    "km": 1000
}
'''
useinput = float(input("give me a number in ft and I'll convert it to meters! "))

#function for converting ft to meters.
def convert(ft):            # function called convert, ft as argument
    m = (ft * 0.3048)       # var called m assigned to operation of ft / 3.208
    return m                # return m variable operation

#created a var called result assigned to the above function, with the user useinput as argument to be fed through function formula
result = convert(useinput)
#printing result to display on the terminal
print(result)
