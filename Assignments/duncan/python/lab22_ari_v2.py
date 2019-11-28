import string
import re

sentence_dict = {}

with open("dracula.txt") as dracula:
    dracula_book = dracula.read()
    dracula_book = dracula_book.lower()
    dracula_words = dracula_book.split(" ")
    print(dracula_words)
    sentences = re.split(r"\.|\!|\?", dracula_sent[0])
    # \ (backslash) sets the following punctuation to be just th punctuation and not a function
    # | (pipe) is teh equvolent of saying "or", i.e. "\.|\!|\?" means . or ! or ?
    print(sentences)

    # for sentence in dracula_sent:
    #     if sentence in dracula_sent:
    #         sentence_split = re.split(". ", dracula_sent[0])
    #         print(sentence_split)

    # for sentence in dracula_sent:
    #     if not sentence:
    #         continue
    #     if sentence in sentence_dict:
    #         sentence_dict[sentence] += 1
    #     else:
    #         sentence_dict[sentence] = 1
