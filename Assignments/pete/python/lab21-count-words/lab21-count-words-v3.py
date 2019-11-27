'''
lab21-count-words-v3.py

Version3

Let the user enter a word, then show the words which most frequently follow it.
'''
import string
user_word = input ("Enter a word to see which words most frequently follow it: ")
#1. Open the file.
with open('franz-kafka-metamorphosis.txt', 'r') as f:
    contents = f.read()
#2. Make everything lowercase,..
    lowercase_contents = contents.lower()
#...strip puncuation...
    lowercase_contents_wo_punctuation = lowercase_contents.translate(str.maketrans('', '', string.punctuation))#I don't get how this works I had to copy and paste
#...split into a list of words.
    word_list = lowercase_contents_wo_punctuation.split()
#...find the words following user word
    user_word_followers = []
    index_counter = 1
    for word in word_list:
        if word == user_word:
            user_word_followers.append(word_list[index_counter])
        index_counter += 1
#3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
    word_count_dict = {}
    for word in user_word_followers:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        if word in word_count_dict:
            word_count_dict[word] += 1
#I'm going to remove boring words (it, a, an, etc.) from the dictionary
boring_words = ['the', 'to', 'and', 'he', 'of', 'his', 'was', 'in', 'it', 'had', 'that', 'a', 'as', 'with', 'not', 'she', 'for', 'him', 'her', 'would', 'at', 'but', 'on', 'they', 'all', 'this', 'be', 'from', 'if', 'or', 'could', 'you', 'out', 'have', 'there', 'been', 'so', 'now', 'gregors', 'any', 'then', 'up', 'back', 'even', 'by', 'into', 'about', 'did', 'himself', 'more', 'their', 'were', 'no', 'when', 'what', 'them', 'way', 'only', 'do', 'one', 'i', 'other', 'than', 'gutenbergtm', 'is', 'just', 'said']
for key in boring_words:
    try:
        word_count_dict.pop(key)
    except:
        pass

#4. Print the most frequent top 10 out with their counts. You can do that with the code below.
    # word_dict is a dictionary where the key is the word and the value is the count
words = list(word_count_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
