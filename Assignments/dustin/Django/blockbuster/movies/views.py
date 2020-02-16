from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Condition, Movie, Genre, Tape

def index(request):
    context = {
        'conditions': Condition.objects.all(),
        'movies': Movie.objects.all(),
        'genres': Genre.objects.all(),
    }
    return render(request, 'movies/index.html', context)

def new_movie(request):
    new_movie = Movie(
        title=request.POST['title'],
        rental_price_cents=500,
        )
    new_movie.save()
    for genre in request.POST.getlist('genres'):
        new_movie.genre.add(genre)
    new_movie.save()
    return HttpResponseRedirect(reverse('movies:index'))

def new_tape(request):
    Tape(
            movie_id = request.POST['movie'],
            condition_id = request.POST['condition']
        ).save()
    return HttpResponseRedirect(reverse('movies:index'))

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Create your views here.
