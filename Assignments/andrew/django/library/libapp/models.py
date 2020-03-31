from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=140)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Title: {self.title}; Publication Date: {self.pub_date}; Author: {self.author}"


class Checkout(models.Model):
    book = models.ForeignKey(
    book, related_name='checkouts', on_delete=models.PROTECT)
    user = models.CharField(max_length=140)
    out = models.BooleanField()

    def __str__(self):
        return f"{self.book}; {self.user}; ("out" if self.out else "in") + ("out" if self.out else "in")"
