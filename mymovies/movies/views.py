from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/index.html", context=context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie_credits = movie.moviecredit_set.all()  # Obtenemos las MovieCre
    context = {'movie': movie ,'movie_credits': movie_credits}
    return render(request, "movies/movie_detail.html", context=context)