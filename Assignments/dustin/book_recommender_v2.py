import requests, random
from bs4 import BeautifulSoup

#Create your own error called InvalidGenreError
class InvalidGenreError(Exception):
    pass

def get_books(genre="horror"):
    # Get HTML data from a website
    response = requests.get(f"https://www.goodreads.com/genres/new_releases/{genre}")
    #if response.status_code == 404:
    #    raise Exception("Invalid genre!")

    # Turn it into something Py can work with
    html = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements on a page
    divs = html.find_all('div')


    books = []

    # Iterate through them
    for div in divs:
        #if they have a class called 'coverWrapper'...
        classes = div.get('class')
        if classes != None and 'coverWrapper' in classes:
            # Find the link and title of the book
            link = div.find('a')['href']
            title = div.find('img')['alt']

            # Add to our books list
            books.append((title, link))
            #print(title, link)
    if len(books) == 0:
        raise Exception("Invalid genre!")

    return books

def get_suggested_books(books, count = 3):
    suggested_books = []
    found = 0

    while found < count:
        suggested_book = random.choice(books)
        if suggested_book not in suggested_books:
            suggested_books.append(suggested_book)
            found += 1
    return suggested_books

def print_suggestions(suggested_books):
    print("  Book Suggestions")
    print("|------------------|")
    for suggested_book in suggested_books:
        title, link = suggested_book
        print(title)
        print(f"https://www.goodreads.com{link}\n")

genre = input("What genre?: ")
count = int(input("How many suggestions?: "))

try:
    books = get_books(genre)
    suggested_books = get_suggested_books(books, count)
    print_suggestions(suggested_books)
except InvalidGenreError as e:
    print(e)
