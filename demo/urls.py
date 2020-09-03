from django.urls import path
from .views import Home, Movies, About, Hello
urlpatterns = [
    path('', Home, name='home'),
    path('movies/<int:id>', Movies, name='movies'),
    path('about/', About, name='about'),
    path('hello/', Hello, name='hello'),
]