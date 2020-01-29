from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Book, Author, Checkout

def index(request):
    return render(request, 'library/index.html', {'books': Book.objects.all()})

def checkout_history(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'library/checkout-history.html', {'checkouts': book.checkouts.all(), 'book': book})

def donate(request):
    return render(request, 'library/donate.html', {'authors': Author.objects.all()})

def checkout_book(request, title):
    if request.method == 'POST':
        book = Book.objects.get(title=title)
        book.available = False
        user = request.POST['user']
        Checkout(checked_out=True, user=user, book=book).save()
        book.save()
        return HttpResponseRedirect(reverse('library:checkout_history', args=[title]))

def return_book(request, title):
    if request.method == 'POST':
        book = Book.objects.get(title=title)
        book.available = True
        user = request.POST['user']
        Checkout(checked_out=False, user=user, book=book).save()
        book.save()
        return HttpResponseRedirect(reverse('library:checkout_history', args=[title]))

def choose_author(request):
    if request.method == 'POST':
        if request.POST['author'] == 'new':
            return new_author(request)
        else:
            return old_author(request)

def new_author(request):
    return render(request, 'library/new-author.html')

def old_author(request):
    author = request.POST['author']
    return render(request, 'library/old-author.html', {'author': Author.objects.get(name=author)})

def old_author_donate(request):
    if request.method == 'POST':
        author = Author.objects.get(name=request.POST['author'])
        Book(title=request.POST['title'], publication_date=request.POST['date'], author=author).save()
        return render(request, 'library/index.html', {'books': Book.objects.all()})

def new_author_donate(request):
    if request.method == 'POST':
        author = Author(name=request.POST['author'])
        author.save()
        Book(title=request.POST['title'], publication_date=request.POST['date'], author=author).save()
        return render(request, 'library/index.html', {'books': Book.objects.all()})