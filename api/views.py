from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

########## Function based api view ##########
'''
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
'''


# Use api_view decoration
@api_view(['GET', 'POST'])
def movies(request):
    # Read
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    # Create
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
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
'''


# Use api_view decoration
@api_view(['GET', 'PUT', 'DELETE'])
def movie(request, movieId):
    try:
        movie = Movie.objects.get(movieId=movieId)

    except Movie.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Read
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # Update
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    # Delete
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########## Function based api view ##########


########## Class based api view ##########
class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieAPIView(APIView):
    def get_object(self, movieId):
        try:
            return Movie.objects.get(movieId=movieId)

        except Movie.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Read
    def get(self, request, movieId):
        movie = self.get_object(movieId)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # Update
    def put(self, request, movieId):
        movie = self.get_object(movieId)
        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def delete(self, request, movieId):
        movie = self.get_object(movieId)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
######### Class based api view #########

######### Generic api view #########
class GenericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = 'movieId'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, movieId = None):
        if movieId:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, movieId = None):
        return self.update(request, movieId)

    def delete(self, request, movieId = None):
        return self.destroy(request, movieId)