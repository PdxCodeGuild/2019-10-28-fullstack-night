from django.shortcuts import render, reverse, redirect
from .models import UrlTask
from string import ascii_letters
import random

# Create your views here.

def index(request):
    if request.method == 'POST':
        long_url1 = UrlTask(long_url=request.POST.get('long_url_input'))
        # long_url1.save()
        # console.log(long_url)
        made_short = ''.join([random.choice(ascii_letters) for i in range(10)])
        UrlTask(long_url=long_url1, shortened_url=made_short).save()
        return redirect(reverse('url_short_app:index'))
    submitted_url = {'urls': UrlTask.objects.all()}
    return render(request, 'url_shortener/index.html', submitted_url)

def redirect_func(request, url_id):
    red_url = Url.object.get(pk=url_id)
    return redirect(red_url.long_url)


# def make_short(request):
#     if request.method == 'POST':
#         long_url = LongUrlTask(long_url=request.POST.get('long_url_input'))
#         long_url.save()
#     context = {}
#     return render(request, "url_shortener/index.html", context)