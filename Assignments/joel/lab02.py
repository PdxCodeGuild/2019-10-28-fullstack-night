'''
Lab: 02
Filename: lab02.py
Author: Joel Weitzel
Objective: Use string concatenation to put each word into the Mad Lib
'''

import random

# user greeting
print("Hello! Welcome to Mad Libs!")

# Input
nouns=input("Please enter 5 nouns seperated by commas: ")
adjectives=input("Please enter 5 adjectives seperated by commas: ")
verbs=input("Please enter 5 verbs seperated by commas: ")

#split the strings into lists
nounsList=nouns.split(",")
#print(nounsList)
adjectivesList=adjectives.split(",")
#print(adjectivesList)
verbsList=verbs.split(",")
#print(verbsList)
#length = len(nounsList)

nounsUsed = []
adjectivesUsed = []
verbsUsed=[]

for x in range(len(nounsList)):
    randomNoun = random.choice(nounsList)
    #if randomNoun in nounsUsed:
        #while randomNoun in nounsUsed:
            #randomNoun = random.choice(nounsList)
    nounsUsed.append(randomNoun)
    randomAdjective = random.choice(adjectivesList)
    adjectivesUsed.append(randomAdjective)
    randomVerb = random.choice(verbsList)
    verbsUsed.append(randomAdjective)
    print("The " + randomAdjective + " " + randomNoun + " " + randomVerb)

    #nounsList.remove(randomNoun)
    #print(nounsList)
    #adjectivesList.remove(randomAdjective)
    #print(adjectivesList)
    #verbsList.remove(randomVerb)
    #print(verbsList)
