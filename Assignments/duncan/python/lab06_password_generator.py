import random

import string

pass_w = ""
s = ""
# a1 = int(input("How many characters long do you want your password? "))

letter_len = int(input("\nHow many alphabetical characters do you want in your password? "))

num_len = int(input("\nHow many numerical characters do you want in your password? "))

punc_len = int(input("\nHow many punctuation characters do you want in your password? "))

for x in range(letter_len):
    pass_w += random.choice(string.ascii_letters)

for x in range(num_len):
    pass_w += random.choice(string.digits)

for x in range(punc_len):
    pass_w += random.choice(string.punctuation)

pass_w = list(pass_w)
random.shuffle(pass_w)
print(s.join(pass_w))


# while game_in_session == "yes" and len(pass_w) < a1:
#     if len(pass_w) < a2:
#         pass_w = pass_w + random.choice(option1)
#     elif len(pass_w) < a2 + a3:
#         pass_w = pass_w + random.choice(option2)
#     elif len(pass_w) < a2 + a3 + a4:
#         pass_w = pass_w + random.choice(option3)
#
# else:
