# Supported unit types
# supported_units = ["ft", "mi", "m", "km"]

units = {
  "ft": 0.3048,
  "mi": 1609.34,
  "m": 1 * 1 * 1,
  "km": 1000
}

# Ask the user for the unit they want
unit = input("What unit do you want: ")

# If an invalid unit is specified, alert the user and exit
if unit not in units.keys():
  print("Please enter a valid unit! Options are ft, mi, m, km...")
  exit()

# Get the amount of units
amount = float(input("How many units: "))

# Look up our unit by the input given
print(f"{amount * units[unit]}m")