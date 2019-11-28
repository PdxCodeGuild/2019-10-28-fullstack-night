'''
filename: madlibs
concept:
    - input()
    - print()
    - fstrings
    - variables
'''

# user greeting
print("Hello! Welcome to Mad Libs!")

### input()
# built-in function that prompts user with a question and allows them to type their answer

# This will prompt the user to answer the question via terminal
first_name = input("What's your name? ")

# \n is used to create a new line within a string
print(f"Glad you're here, {first_name}!\n")

space_obj = input("What is an object that is in space? ")
place = input("Where are you? ")
birth_stone = input("What is your birth stone? ")
question = input("Ask me a question. ")

# print(''' is an alternative means of creating a string with multiple lines
print(f'''\nTwinkle, twinkle, little {space_obj},
How I wonder what you are!
Up above {place} so high,
Like a {birth_stone} in the sky.
Twinkle, twinkle, little {space_obj},
How I wonder {question}
''')
