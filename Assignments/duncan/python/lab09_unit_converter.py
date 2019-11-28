units = ["ft", "mi", "m", "km", "yd", "in"]

# feet = float(input("What is the distance in feet? "))
# meters = feet * 0.3048
# print(f"{feet} ft is {round(meters, 5)} m.")

game_in_session = "yes"

while game_in_session == "yes":
    user_choice = input("What unit of measurement do you want to convert; ft, mi, m, km, yd, or in? ")
    if user_choice == "ft":
        feet = float(input("What is the distance in ft? "))
        meters = feet * 0.3048
        print(f"{feet} ft is {round(meters, 5)} m.")
    elif user_choice == "mi":
        miles = float(input("What is the distance in miles? "))
        meters = miles * 1609.34
        print(f"{miles} mi is {round(meters, 5)} m.")
    elif user_choice == "km":
        kilometers = float(input("What is the distance in kilometers? "))
        meters = kilometers * 1000
        print(f"{kilometers} km is {round(meters, 5)} m.")
    elif user_choice == "m":
        meters = float(input("What is the distance in meters? "))
        print(f"{meters} m is {meters} m. Like, comeon.")
    elif user_choice == "yd":
        yards = float(input("What is the distance in yards? "))
        meters = yards * 0.9144
        print(f"{yards} yd is {round(meters, 5)} m.")
    elif user_choice == "in":
        inches = float(input("What is the distance in inches? "))
        meters = inches * 0.0254
        print(f"{inches} in is {round(meters, 5)} m.")
    elif user_choice not in units:
        print("Error!")
    game_in_session = input("Do you want to convert a different unit of measurement or distance into meters? ").lower()
else:
    print("Goodbye.")


# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
