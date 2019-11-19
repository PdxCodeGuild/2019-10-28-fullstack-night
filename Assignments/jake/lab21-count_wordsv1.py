import string

with open('philosophy_book.txt', 'r') as f:
    contents = f.read()

    lowercase_contents = contents.lower()

    lowercase_contents_wo_punctuation = lowercase_contents.translate(str.maketrans('', '', string.punctuation))

    word_list = lowercase_contents_wo_punctuation.split()

    word_count_dict = {}
    for word in word_list:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        if word in word_count_dict:
            word_count_dict[word] += 1



boring_words = ['the', 'to', 'and', 'he', 'of', 'his', 'was', 'in', 'it', 'had', 'that', 'a', 'as', 'with', 'not', 'she', 'for', 'him', 'her', 'would', 'at', 'but', 'on', 'they', 'all', 'this', 'be', 'from', 'if', 'or', 'could', 'you', 'out', 'have', 'there', 'been', 'so', 'now', 'gregors', 'any', 'then', 'up', 'back', 'even', 'by', 'into', 'about', 'did', 'himself', 'more', 'their', 'were', 'no', 'when', 'what', 'them', 'way', 'only', 'do', 'one', 'i', 'other', 'than', 'gutenbergtm', 'is', 'just', 'said']
for key in boring_words:
    word_count_dict.pop(key)


words = list(word_count_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
