import requests
import random
from bs4 import BeautifulSoup

# Create your own error called InvalidGenreError 
class InvalidGenreError(Exception):
  pass

def get_books(genre='horror'):
  # Get html data from a website
  response = requests.get(f"https://www.goodreads.com/genres/new_releases/{genre}")

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

  # If we find no books, raise an error
  if len(books) == 0:
    raise InvalidGenreError("Invalid genre!")

  return books

def get_suggested_books(books, count=3):
  # Setup our suggest books list
  suggested_books = []
  # Start our books_found counter at 0
  books_found = 0

  # Make sure we don't loop forever
  count = min(len(books), count)

  # While we haven't found 3 books...
  while books_found < count:
    # Randomly pick a book
    suggested_book = random.choice(books)
    # If it hasn't already been picked...
    if suggested_book not in suggested_books:
      # Add it to our list 
      suggested_books.append(suggested_book)
      # Increase the amount of books we've found
      books_found += 1
  
  return suggested_books

def print_suggestions(suggested_books):
  # Print our suggested books in a nice way
  print(f"We suggest these {len(suggested_books)} book(s):")
  print("-----------------------\n")
  for suggested_book in suggested_books:
    # Tuple unpack our title and link
    title, link = suggested_book
    print(title)
    print(f"https://www.goodreads.com{link}\n")

# Default setup!
# books = get_books()
# suggested_books = get_suggested_books(books)
# print_suggestions(suggested_books)

# Take user input
genre = input("What genre do you want?: ")
count = int(input("How many do you want?: "))

# Try and get books, and catch an invalid genre
try:
  books = get_books(genre)
  suggested_books = get_suggested_books(books, count)
  print_suggestions(suggested_books)
except InvalidGenreError as e:
  print(e)