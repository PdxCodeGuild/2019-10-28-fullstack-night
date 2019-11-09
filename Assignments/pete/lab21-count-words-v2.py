'''
lab21-count-words-v1.py
Version1

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.
'''
import string
#1. Open the file.
with open('franz-kafka-metamorphosis.txt', 'r') as f:
    contents = f.read()
#2. Make everything lowercase,..
    lowercase_contents = contents.lower()
#...strip puncuation...
    lowercase_contents_wo_punctuation = lowercase_contents.translate(str.maketrans('', '', string.punctuation))#I don't get how this works I had to copy and paste
#...split into a list of words.
    word_list = lowercase_contents_wo_punctuation.split()
#3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
    word_count_dict = {}
    for word in word_list:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        if word in word_count_dict:
            word_count_dict[word] += 1

# print(contents)
# print(lowercase_contents)
# print(lowercase_contents_wo_punctuation)
# print(word_list)
# print(word_count_dict)

'''
Version 2

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.
'''
#I'm going to remove boring words (it, a, an, etc.) from the dictionary
boring_words = ['the', 'to', 'and', 'he', 'of', 'his', 'was', 'in', 'it', 'had', 'that', 'a', 'as', 'with', 'not', 'she', 'for', 'him', 'her', 'would', 'at', 'but', 'on', 'they', 'all', 'this', 'be', 'from', 'if', 'or', 'could', 'you', 'out', 'have', 'there', 'been', 'so', 'now', 'gregors', 'any', 'then', 'up', 'back', 'even', 'by', 'into', 'about', 'did', 'himself', 'more', 'their', 'were', 'no', 'when', 'what', 'them', 'way', 'only', 'do', 'one', 'i', 'other', 'than', 'gutenbergtm', 'is', 'just', 'said']
for key in boring_words:
    word_count_dict.pop(key)

#4. Print the most frequent top 10 out with their counts. You can do that with the code below.
    # word_dict is a dictionary where the key is the word and the value is the count
words = list(word_count_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
