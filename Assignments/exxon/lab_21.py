import string


STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]



with open('aztec.txt', 'r') as aztec_book:

    contents = aztec_book.read()





def main():



    new_book_format = contents
    translator = str.maketrans('', '', string.punctuation)
    no_punct_new_book_format = new_book_format.translate(translator)
    no_punct_new_book_format = no_punct_new_book_format.lower()
    no_punct_new_book_format = no_punct_new_book_format.strip()
    no_punct_new_book_format = no_punct_new_book_format.split()
    
    book_count(no_punct_new_book_format)
    

def book_count(no_punct_new_book_format):

    book_dict = {}
    no_punct_new_book_format = tuple(no_punct_new_book_format)
    for word in no_punct_new_book_format:
        if word not in book_dict:
            book_dict[word] = 0
            book_dict[word] += 1
        if word in no_punct_new_book_format:
            book_dict[word] += 1
    






    words = book_dict
    words = list(book_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    words = [word for word in words if word[0] not in STOPWORDS]
    print("The most common words are: ")
    print('\n')
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    
        print(words[i])


main()















