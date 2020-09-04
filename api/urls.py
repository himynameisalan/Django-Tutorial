from django.urls import path
from .views import movies, movie, MoviesAPIView, MovieAPIView, GenericAPIView

urlpatterns = [
    # Function based api view
    # path('movies/', movies),
    # path('movie/<str:movieId>', movie)

    # Class based api view
    path('movies/', MoviesAPIView.as_view()),
    path('movie/<str:movieId>/', MovieAPIView.as_view()),

    # Generic api view
    path('generic/movies/', GenericAPIView.as_view()),
    path('generic/movie/<str:movieId>/', GenericAPIView.as_view()),
]
