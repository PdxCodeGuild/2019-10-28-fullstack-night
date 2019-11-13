'''
By: Dustin DeShane
Filename: lab21.py
'''
import string

with open('MobyDickUTF8.txt', 'r', encoding='UTF-8') as moby_dick:

    moby_read = moby_dick.read().lower() #reads file in as lower case letters
    moby_list = list(moby_read) #converts string to list
    moby_after = []
    moby_usable = ""
    moby_dict = {}
    moby_wordlist = []

    for k in range(0, len(moby_list)): #iterates through list
        letter = moby_list[k]
        if letter in string.ascii_lowercase or letter in string.whitespace: #removed punctuation from text
            moby_after.append(letter)
    for k in range(0, len(moby_after)):
        moby_usable = moby_usable + moby_after[k] #converts back to string

    moby_wordlist = moby_usable.split() #converts into list of words

    for i, word in enumerate(moby_wordlist): #build dictionary
        if word not in moby_dict.keys():
            moby_dict[word] = 1 #initialize entry
        elif word in moby_dict.keys():
            moby_dict[word] = moby_dict[word] + 1 #increase count if entry already exists
        else:
            pass
    
    # added from lab instructions
    words = list(moby_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    #print(moby_dict)