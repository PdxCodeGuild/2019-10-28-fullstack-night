'''
Lab 22: Compute Automated Readability Index
Version1
https://github.com/PdxCodeGuild/2019-10-28-fullstack-night/blob/master/1%20Python/labs/lab22-ari.md
'''
import string
import math
import re
book = input("Which book: ") or 'Lewis-Carrol-Alices-Adventures-in-Wonderland.txt'
#open the file
with open(book, 'r') as f:
    contents = f.read()
    #make lowercase
    lowercase_contents = contents.lower()
    #strip all punctuation for words list
    lowercase_contents_wo_punctuation = lowercase_contents.translate(str.maketrans('', '', string.punctuation))
    #continue to turn it into a list
    word_list = lowercase_contents_wo_punctuation.split()
    #count the words
    word_count = 0
    for word in word_list:
        word_count += 1
    #for the characters, replace every ' ' with ''
    characters = lowercase_contents_wo_punctuation.replace(' ', '')
    #get the count of all the characters (minus 2 for the first and last ')
    character_count = len(characters) -2
    #sentences
    sentences = re.split(r'\.|\?|\!', lowercase_contents)
    #sentence count
    sentence_count = 0
    for sentence in sentences:
        sentence_count += 1

#ARI
ari = math.ceil(4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43)
if ari > 14:
    ari = 14
print(f"word_count: {word_count}")
print(f"character_count: {character_count}")
print(f"sentence_count: {sentence_count}")
print(f"ari: {ari}")

#ARI scale dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
print(f"{book} has an ARI of {ari}.\nIt has a {ari_scale[ari]['grade_level']} reading level and is suited for persons aged {ari_scale[ari]['ages']}")