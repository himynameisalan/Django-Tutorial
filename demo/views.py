from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movie

# Create your views here.

# def Home(request):
#   return HttpResponse("<h1>Homepage</h1>")
def Home(request):
  contest = {
    'id' : 'A123456789',
    'name' : 'Django',
  }
  return render(request, 'home.html', contest)

def Movies(request, id):
  # Retrieve data from database
  obj = Movie.objects.get(movieId = id)

  contest = {
    'data' : obj,
    'movieId' : id,
    'title' : obj.title
  }

  return render(request, 'movies.html', contest)

def About(request):
  contest = {
    'list' : [1, 2, 3, 4]
  }
  return render(request, 'about.html', contest)

def Hello(request):
  return HttpResponse("<h1>hello world!</h1>")