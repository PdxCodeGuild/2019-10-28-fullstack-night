from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Book, Author, Checkout

def index(request):
    return render(request, 'library/index.html', {'books': Book.objects.all()})

def checkout_history(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'library/checkout-history.html', {'checkouts': book.checkouts.all(), 'book': book})

def donate(request):
    return render(request, 'library/donate.html')

def checkout_book(request, title):
    if request.method == 'POST':
        book = Book.objects.get(title=title)
        book.available = False
        user = request.POST['user']
        Checkout(checked_out=True, user=user, book=book).save()
        return HttpResponseRedirect(reverse('library:index'))
    return render(request, 'library/confirm.html', {})

def return_book(request, title):
    pass