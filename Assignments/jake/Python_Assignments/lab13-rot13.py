import codecs

phrase = input("Write a word: ")

enc = codecs.getencoder( "rot-13")

os = enc(phrase) [0] #the [0] leaves the number of letters in the word out

print( os )

'''Lots of research for importing codecs and getencoder was done on github and w3schools'''