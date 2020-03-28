import string

word1 = input('enter first word')

word2 = input('enter second word')

def anagram(word1, word2):
    
    '''
    word1 = list(word1)
    '''
    word1 = word1.sort()
    '''
    word2 = list(word2)
    '''
    word2 = word2.sort()
    return (word1, word2)
print(word1, word2)


