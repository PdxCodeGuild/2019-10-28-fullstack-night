"""
Lab 2
DJ Thomas
10-29-2019
filename: lab_02_mad_libs.py

lab covers the following:
    - print('')
    - datatype: strings
    - input()
    - print(f'')
    - new line: \n and print()
"""

print()
print('Welcome to Madlibs. Please fill out the questions below to create your story!\n\n\n')

print('       Title: Missing Person')
pirate =input('If you were a pirate what would your name be: ')
traveled =input('Where is the craziest place you have ever traveled to: ')
power =input('If you could have a super power what would it be: ')
age =input('How old are you: ')


print()
print('Congratualtions on completing your first Madlib!\n')

print(f'We are looking for a person which goes by the name of {pirate}. He was last seen in the middle of {traveled}. Before he went missing, his mother stated {pirate} thinks a slice of pizza has {power}. {pirate} has been missing for {age}. If you have any information regarding the where abouts of {pirate} please contact Zach at Code Guild.\n\n\n')
