def cipher(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'nopqrstuvwxyzabcdefghijklm'
    encrypted = ''
    for i in range(0, len(string)):
        index_of_origin = letters.index(string[i])
        encrypted = encrypted + cipher[index_of_origin]
        # encrypted = encrypted + cipher[index_of_origin]
    return encrypted


word = input('What would you like to encrypt? ').lower()
rotations = input('please type number of rotations (1 - 10)')
word2 = word.replace(" ", "")
cipher(word2)
encrypted_word = cipher(word2)
print(f'Original text: {word} \nEncrypted word: {encrypted_word}')