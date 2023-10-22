from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path('genre/<int:genre_id>/', views.genre_movies, name='genre_movies'),
]