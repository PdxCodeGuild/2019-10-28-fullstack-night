import random

v_eyes = ["o o", ". .", "- -", "o 0"]
v_nose = [" L ", " l ", " c "]
v_mouth = [" ~ ", " - ", " O "]

h_eyes = [":", ";", "="]
h_nose = ["-", "v", "~"]
h_mouth = ["o", "3", "*"]

print("Welcome to the emoji generator")

v_emoji = (f"\n{random.choice(v_eyes)}\n{random.choice(v_nose)}\n{random.choice(v_mouth)}")

h_emoji = (f"{random.choice(h_eyes)} {random.choice(h_nose)} {random.choice(h_mouth)}")

emoji = "yes"
game_in_session = "yes"

while game_in_session == "yes":
    emoji = input("\nDo you want a vertical face?: ").lower()
    if emoji == "yes":
        eyes = input(str("Do you want to manually create the eyes for the emoji?")).lower()
        if eyes = "yes"

        # Working on creating the manual creation of emoji T.B.D.!!!

        print(v_emoji)
        for x in range(4):
            print(v_emoji)

    elif emoji == "no":
        print(h_emoji)
        for x in range(4):
            print(h_emoji)

    else:
        print("Invalid response.")
    game_in_session = input("Do you want to create another emoji? ").lower()

else:
    print("Goodbye.")
