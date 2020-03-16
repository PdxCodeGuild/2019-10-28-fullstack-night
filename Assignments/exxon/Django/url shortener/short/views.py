from django.shortcuts import render
from .models import URL
from django.urls  import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, render

import random
import string


def code_gen():

    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 6
    return ''.join(random.choice(chars) for num in range(size))






def index(request):

    long_urls = URL.objects.all()
    context = {'long_urls':long_urls}
    
    return render(request, 'short/index.html', context)




def coder(request):
    short_url = code_gen()
    URL.objects.create(pub_date=timezone.now(), url_text=request.POST['url_name'], short_url=short_url)
    short_message = f"New Code: {short_url} - To use in browser, erase short/ and add success/{short_url} to existing URL."
    messages.success(request, short_message)

    return HttpResponseRedirect(reverse('short:index'))


def success(request,short_url):
    
    user_url = get_object_or_404(URL, short_url=short_url)
    new_url = user_url.url_text                                 # what does this line do?

    return HttpResponseRedirect(new_url)

    #new short code works but you need to erase the shorts/ at beginning of url?