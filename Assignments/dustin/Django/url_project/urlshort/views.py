from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import LinkStart
from string import ascii_letters
import random

def random_gen(request):
    output = ''
    outputList = []
    option_list = list(ascii_letters)
    for i in range(0, 10):
        option_list.append(i)
    for i in range(0, 9):
        randomSelect = str(option_list[random.randint(0, len(option_list)-1)])
        outputList.append(randomSelect)
        output = output + outputList[i]
    
    return output

        
def pullBaseURL(request):
    data = request.POST
    slashCount = 0
    baseURL = ""
    baseList = []
    for i, val in enumerate(data):
        if val == "/":
            slashCount += 1
            if slashCount == 3:
                break
        baseList.append(val)
        baseURL = baseURL + baseList[i]
    return baseURL

def shortenedURL(request):
    data = request.POST
    newURL = data["baseURL"] + "/" + data["output"]
    return newURL



        
    
    

def shorten(request):
    pass

# Create your views here.
