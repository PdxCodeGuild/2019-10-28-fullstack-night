from django.shortcuts import render
from .models import Book, Author

def index(request):
    authors = Author.objects.all()
    return render(request, 'library_app/index.html', {'authors': authors})

def author_detail(request, pk):
    active_author = Author.objects.get(pk=pk)
    books = active_author.book_set.all()
    return render(request, 'library_app/author.html', {'author': active_author, 'books': books})

# Create your views here.
