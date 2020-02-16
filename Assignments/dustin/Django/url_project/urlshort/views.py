from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import LinkStart
from string import ascii_letters
import random

def index(request):
    if request.method=="POST":
        data = request.POST
        longURL = LinkStart(url_in=data['url_in'], code=random_gen())
        longURL.save()
        print(longURL.url_in)
    context = {}
    return render(request, "urlshort/index.html", context)
    #return HttpResponse("Hi.")

def redir(request, user_url):
    longURL = LinkStart.objects.get(code=user_url)
    print(longURL.url_in)
    return HttpResponseRedirect("http://" + longURL.url_in)


def random_gen():
    output = ''
    outputList = []
    option_list = list(ascii_letters)
    for i in range(0, 10):
        option_list.append(i)
    for i in range(0, 9):
        randomSelect = str(option_list[random.randint(0, len(option_list)-1)])
        outputList.append(randomSelect)
        output = output + outputList[i]
    print(output)
    return output
  

def shorten(request):
    pass

# Create your views here.
