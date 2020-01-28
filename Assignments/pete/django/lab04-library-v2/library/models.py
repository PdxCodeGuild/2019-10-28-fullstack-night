from django.db import models

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
class Book(models.Model):
    title = models.CharField(max_length=140)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Author: a model representing an author of a book, one author can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=140)