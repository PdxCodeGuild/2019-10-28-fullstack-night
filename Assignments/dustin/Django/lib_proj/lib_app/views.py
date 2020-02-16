from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'lib_app/index.html', {})

def author_detail(request, pk):
    #data = request.GET(pk=pk)
    author = Author.objects.get(pk=pk)
    print(author)
    return render(request, 'lib_app/author_detail.html', {'author': author})

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
