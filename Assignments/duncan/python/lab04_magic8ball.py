import random

mag8_resp = ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print("Welcome to the digital magic 8 ball!\n")

input("What is your question?")

mag8_answ = random.choice(mag8_resp)

print(mag8_answ)

a1 = input("Do you have another question?")

while a1 == "yes":
    input("What is your question?")
    print(mag8_answ)
    a1 = input("\nDo you have another question?")
else:
    print("Goodbye.")
