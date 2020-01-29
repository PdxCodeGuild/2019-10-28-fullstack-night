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
    # return render(request, 'library/confirm.html', {})

def return_book(request, title):
    if request.method == 'POST':
        book = Book.objects.get(title=title)
        book.available = True
        user = request.POST['user']
        Checkout(checked_out=False, user=user, book=book).save()
        book.save()
        return HttpResponseRedirect(reverse('library:checkout_history', args=[title]))
    # return render(request, 'library/checkokut-history.html', {'checkouts': book.checkouts.all(), 'book': book})

def choose_author(request, author):
    if request.method == 'POST':
        if request.POST['author'] == 'new':
            #go about adding new author
            # return render(request, 'library/new-author.html')
            new_author(request)
        else:
            old_author(request, author)
            # return render(request, 'library/old-author.html', {'author': Author.objects.get(name=request.POST['author'])})

def new_author(request):
    return render(request, 'library/new-author.html')

def old_author(request, author):
    return render(request, 'library/old-author.html', {'author': Author.objects.get(name=author)})