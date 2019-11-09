import requests
import random
from bs4 import BeautifulSoup

# Get html data from a website
response = requests.get("https://www.goodreads.com/genres/new_releases/horror")

# Turn it into something python can work with
html = BeautifulSoup(response.text, 'html.parser')

# Find all div elements on a page
divs = html.find_all('div')

# Found books
books = []

# Loop over them
for div in divs:
  classes = div.get('class')
  # If they have a class called 'coverWrapper'...
  if classes and 'coverWrapper' in classes:
    # Find the link and title of the book
    title = div.find('img')['alt']
    link = div.find('a')['href']
    # Add to our books list
    book = (title, link)
    books.append(book)

# Setup our suggest books list
suggested_books = []
# Start our books_found counter at 0
books_found = 0

# While we haven't found 3 books...
while books_found < 3:
  # Randomly pick a book
  suggested_book = random.choice(books)
  # If it hasn't already been picked...
  if suggested_book not in suggested_books:
    # Add it to our list 
    suggested_books.append(suggested_book)
    # Increase the amount of books we've found
    books_found += 1

# Print our suggested books in a nice way
print("We suggest these books:")
print("-----------------------\n")
for suggested_book in suggested_books:
  # Tuple unpack our title and link
  title, link = suggested_book
  print(title)
  print(f"https://www.goodreads.com{link}\n")