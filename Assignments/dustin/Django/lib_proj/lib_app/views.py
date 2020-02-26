from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author, CheckoutStatus
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'lib_app/index.html', {})

def checkout_history(request):
    data = CheckoutStatus.objects.all()
    return render(request, 'lib_app/checkout_status.html', {'status': data})

def author_detail(request, pk):
    #data = request.GET(pk=pk)
    author = Author.objects.get(pk=pk)
    print(author)
    return render(request, 'lib_app/author_detail.html', {'author': author})

def checkout_book(request, pk):
    book = Book.objects.get(pk=pk)
    data = book.author
    book.checked_out = True
    book.save()
    status = CheckoutStatus(book=book, status=book.checked_out, user=request.user)
    status.save()
    return HttpResponseRedirect(reverse('lib:author_detail', kwargs={'pk': data.pk}))

def search(request):
    data = request.GET
    search_choice = data.get("search_choice")

    if search_choice == "Book":
        results = search_books(data)
        print(results)
    if search_choice == "Author":
        results = search_authors(data)
        print(results)
    #return None
    return render(request, 'lib_app/index.html', {'results': results})

    return HttpResponseRedirect(reverse('lib:index'))

def search_books(data):
    results = Book.objects.filter(title__icontains=data.get("user_input"))
    print(results)
    return results
    

def search_authors(data):
    # if select_id = Author, filter search based on Author.name
    results = Author.objects.filter(name__icontains=data.get("user_input"))
    print(results)
    return results
    


# Create your views here.
