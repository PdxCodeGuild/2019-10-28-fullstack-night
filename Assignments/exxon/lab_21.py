
#  open file 

with open('aztec.txt', 'r') as aztec_book:

    contents = aztec_book.read()



#  function to format book to have all lower case letters, no empty spaces between words, removing trailing and ending spaces

def stripped_book(book):
    new_book_format = contents.lower()
    new_book_format = new_book_format.strip()
    new_book_format = new_book_format.replace(" ", "")
    print (new_book_format)




#  running file through formatting function

stripped_book(contents)

