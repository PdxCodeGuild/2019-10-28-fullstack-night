from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect

from .models import Url

from string import ascii_letters

from random import choice

"""
Your app should contain the following:
"""

def index(request):
    """
    one view that returns a page for entering in a url to be shortened, and possibly a list of entries (localhost/urlshorten/index/)
    """
    return render(request, 'shortener/index.html', {'urls': Url.objects.all()})
    # return HttpResponseRedirect(reverse(('shortener:index')))
    # return HttpResponse("So you're thinking about shortening a url.")

def shorten(request):
    """
    another view and view for receiving the POSTed url, generating a random string, and saving it to the database (localhost/urlshorten/saveurl)
    """
    if request.method == 'POST':
        in_url = request.POST['long-url']
        out_url = ''.join([choice(ascii_letters + '1234567890') for i in range(6)])
        Url(long_url=in_url, short_url=out_url).save()
        return HttpResponseRedirect(reverse('shortener:index')) ##what does reverse do, exactly?
    return render(request, 'shortener/index.html', {'urls': Url.objects.all()})

def redirect_url(request, pk):
    """
    a third view that performs the redirecting (localhost/redirect/pEc4vt), you should use redirect instead of HttpResponseRedirect.
    """
    data_set = Url.objects.get(pk=pk)
    return redirect(data_set.long_url)
    #above I had return redirect(data_set.long_url())

