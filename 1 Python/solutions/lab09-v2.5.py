# Supported unit types
supported_units = ["ft", "mi", "m", "km"]

# Ask the user for the unit they want
unit = input("What unit do you want: ")

# If an invalid unit is specified, alert the user and exit
if unit not in supported_units:
  print("Please enter a valid unit! Options are ft, mi, m, km...")
  exit()

# Get the amount of units
amount = float(input("How many units: "))

# Check to see if the unit matches one we know
if unit == "ft":
  print(amount * 0.3048)
elif unit == "mi":
  print(amount * 1609.34)
elif unit == "m":
  print(amount * 1 * 1 * 1) # Extra spicy
elif unit == "km":
  print(amount * 1000)