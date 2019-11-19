import requests, random
from bs4 import BeautifulSoup

# Get HTML data from a website
response = requests.get("https://www.goodreads.com/genres/new_releases/horror")

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

suggested_books = []
found = 0

while found < 3:
    suggested_book = random.choice(books)
    if suggested_book not in suggested_books:
        suggested_books.append(suggested_book)
        found += 1
print("  Book Suggestions")
print("|------------------|")
for suggested_book in suggested_books:
    title, link = suggested_book
    print(title)
    print(f"https://www.goodreads.com{link}\n")