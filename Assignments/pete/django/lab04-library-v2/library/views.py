from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Author, Checkout

def index(request):
    return render(request, 'library/index.html', {'books': Book.objects.all()})

def checkout_history(request, title):
    return render(request, 'library/checkout.html', {'checkouts': Checkout.objects.get(book=Book.objects.get(title=title)), 'book': Book.objects.get(title=title).all()})