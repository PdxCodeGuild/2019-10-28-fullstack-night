from django.db import models

# Author: a model representing an author of a book, one author can have multiple books
class Author(models.Model):

    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
class Book(models.Model):
    
    title = models.CharField(max_length=140)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}; Publication Date: {self.publication_date}; Author: {self.author}"



class Checkout(models.Model):
# book: the book that the user checked out or checked in
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
# user: a text field containing the name of the user that checked out or checked in the book
    user = models.CharField(max_length=140)
# checkout: a boolean indicating whether the book was checked out or checked in
    checked_out = models.BooleanField()
# timestamp: a datetime that records when the book was checked out or in
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book: {self.book}; User: {self.user}; Status: " + ("Checked Out" if self.checked_out else "Available") + "; " + ("Checked Out" if self.checked_out else "Returned") + f": {self.timestamp}"