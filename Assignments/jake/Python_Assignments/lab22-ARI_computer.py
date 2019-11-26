import string
import math

with open('philosophy_book.txt', 'r', encoding='UTF-8') as philosophy_book:

    phil_read = philosophy_book.read().lower() #reads file in as lower case letters
    phil_list = list(phil_read) #converts string to list
    phil_after = []
    phil_usable = ""
    sentences = 0
    words_total = 0
    characters_total = 0

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
    14: {'ages': '18-22', 'grade_level':      'College'},
    }

    for k in range(0, len(phil_list)): #iterates through list
        letter = phil_list[k]
        if letter in string.ascii_lowercase: #count number of characters
            characters_total += 1
        if letter in string.ascii_lowercase or letter in string.whitespace or letter == ".": #removed punctuationexcept . from text
            phil_after.append(letter)
    for k in range(0, len(phil_after)):
        phil_usable = phil_usable + phil_after[k] #converts back to string
    
    for words in phil_usable:
        if words.endswith("."): #count sentences
            sentences += 1
        elif words.endswith(" "): #count words(non-total)
            words_total += 1
    
    words_total = words_total + sentences #calculate total words

    print(f"Sentences: {sentences}")
    print(f"Words: {words_total}")
    print(f"Characters: {characters_total}")

    ari_calc = float((4.71*characters_total)/words_total)+float((0.5*words_total)/sentences)-21.43 #calculate ARI

    print(f"ARI: {math.ceil(ari_calc)}") #print rounded up ARI

    if math.ceil(ari_calc) > 14: #adjusts all values > 14 ARI down to 14
        ari_calc = 14

    for ari in ari_scale.keys():
        if math.ceil(ari_calc) == ari:
            print(f"This corresponds to a {ari_scale[ari]['grade_level']} grade level and is suitable for an average person of ages {ari_scale[ari]['ages']}.")
        
        