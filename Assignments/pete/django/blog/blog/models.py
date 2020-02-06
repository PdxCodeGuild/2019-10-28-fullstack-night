from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140)
    body = models.CharField(max_length=20000)
    def __str__(self):
        return f"Author: {self.author}; Publication Date: {self.pub_date}; Title: {self.title}"