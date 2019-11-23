with open('grimm.txt', 'r', encoding = 'utf-8') as grimm_fairytails:
    contents = grimm_fairytails.read()
    contents = str.lower(contents)
    punctuation = '''''!()-[]{};:'",<''>.?@#$%^&*_~'''  
    no_punct = ""
    for char in contents:  
        if char not in punctuation:  
            no_punct = no_punct + char 
    no_punct = no_punct.split()
    wordcount = {}
    for word in no_punct:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            
words = list(wordcount.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])