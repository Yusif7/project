from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator


def movies(request):
    movie_objects = Movies.objects.all()

    # Search filter
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    movie_name = request.GET.get('movie_all')
    if movie_name != '' and movie_name is not None:
        movie_objects = Movies.objects.all()

    # Paginations logic
    paginator = Paginator(movie_objects, 3)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)

    # /?page=2
    context = {
        'movie_objects': movie_objects
    }
    return render(request, 'movies.html', context)
