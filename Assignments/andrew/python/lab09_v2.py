unit = input("What unit would you like to convert to meters? feet, miles, kilometers, meters, yards, or inches?")
distance = input("What is the distance?")
conversion_m_f = .3048
conversion_m_mi = 1609.34
conversion_m_m = 1
conversion_km = 1000

if unit == "feet":
    output = int(distance) * conversion_m_f
elif unit == "miles":
    output = int(distance) * conversion_m_mi
elif unit == "kilometers":
    output = int(distance) * conversion_km
elif unit == "meters":
    output = int(distance) * conversion_m_m

print(f"{distance} {unit} is {output} meters")
