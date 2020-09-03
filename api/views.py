from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt.
@csrf_exempt
def movies(request):
  # Read
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return JsonResponse(serializer.data, safe = False)
  # Create
  elif request.method == 'POST':
    data = JSONParser(request)
    serializer = MovieSerializer(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.error, status = 400)

# Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt.
@csrf_exempt
def movie(request, id):
  try: 
    movie = Movie.objects.get(movieId = id)
  
  except Movie.DoesNotExist:
    return HttpResponse(status = 404)

  # Read
  if request.method == 'GET':
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)
  # Update
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = MovieSerializer(movie, data = data)
     
    if serializer.is_valid():
      serializer.save() 
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)
  # Delete
  elif request.method == 'DELETE':
    movie.delete()
    return HttpResponse(status = 204)