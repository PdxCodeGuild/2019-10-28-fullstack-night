# Supported unit types
# supported_units = ["ft", "mi", "m", "km"]

units = {
  "ft": 0.3048,
  "mi": 1609.34,
  "m": 1 * 1 * 1,
  "km": 1000,
  "yard": 0.9144, # Easy...
  "inch": 0.0254, # Peasy!
}

# Ask the user for the unit they want
from_unit = input("Convert from: ")
to_unit = input("Convert to: ")

# If an invalid unit is specified, alert the user and exit
if from_unit not in units.keys() or to_unit not in units.keys():
  print("Please enter a valid units! Options are ft, mi, m, km...")
  exit()

# Get the amount of units
amount = float(input("How many units: "))

# Look up our unit by the input given
value_in_meters = amount * units[from_unit]
value_in_to_unit = value_in_meters / units[to_unit]

print(f"{value_in_to_unit}{to_unit}")