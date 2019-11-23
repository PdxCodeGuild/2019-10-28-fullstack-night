user_input = input("What would you like to translate?")

rot_13 = bytes.maketrans(b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")


print(user_input.translate(rot_13))
