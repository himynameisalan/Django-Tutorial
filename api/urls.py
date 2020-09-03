from django.urls import path
from .views import movies, movie

urlpatterns = [
    path('movies/', movies),
    path('movie/<str:movieId>', movie)
]