import requests
import random
from bs4 import BeautifulSoup


#get html data from a website
response = requests.get("https://www.goodreads.com/genres/horror")

#turn it into something python can work with
html = BeautifulSoup(response.text, 'html.parser')

#find all div elements on a page
divs = html.find_all('div')

#found books
books = []

#loop over them
for div in divs:
    classes = div.get('class')
    #if they have a class called 'coverWrapper'...
    if classes and 'coverWrapper' in classes:
        #find the link and title of the book
        title = div.find('img')['alt']
        link = div.find('a')['href']
       
        books.append (books)
#setup our suggest book list
suggested_books = []
#start our books_found counter at 0
found = 0

#while we habent found 3 books
while found < 3:
    #randomly pick a book
    suggested_books = random.choice(books)
    #if it hasnt already been picked
    if suggested_books not in suggested_books:
        #add it to our list
        #increase the amount of books we've found
        books_found += 1

print ('we suggest these books... ')
print ('--------------------------')
for suggested_books in suggested_books:
    print('title')
    print(f'https://www.goodreads.com/genres/horror {link}\n')