'''
By: Dustin DeShane
Filename: lab17.py
'''
import string

user_in = input("Please enter a word to see if it is a palindrome: ")
user_list = list(user_in)
before = list(user_in)
user_list.reverse()
after = user_list

if before == after:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome.")

print("\n\nAnagram check:\n\n")

wordone = input("Please enter a word or string of words: ").lower().replace(" ","")
wordtwo = input("Please enter another word or string of words: ").lower().replace(" ","")


#punctuation removal
wordoneedit = wordone.translate(str.maketrans('', '', string.punctuation))
wordtwoedit = wordtwo.translate(str.maketrans('', '', string.punctuation))

# match inputs for evaluation
listone = list(wordoneedit)
listone.sort()
listtwo = list(wordtwoedit)
listtwo.sort()

'''
### Alternative punctuation removal ###
listone = []
listtwo = []
for k in wordone:
    if k not in list(string.punctuation):
        listone.append(k)
for k in wordtwo:
    if k not in list(string.punctuation):
        listtwo.append(k)
listone.sort()
listtwo.sort()
'''

#compare sorted inputs
if listone == listtwo:
    print("Yes, your words are anagrams!")
else:
    print("No, your word's aren't anagrams.")
#print(listone)
#print(listtwo)