from rest_framework import serializers
from .models import Movie, Rating

## Serializer
class MovieSerializer(serializers.Serializer):
  movieId = serializers.CharField(max_length = 100)
  title = serializers.CharField(max_length = 100)
  genres = serializers.CharField(max_length = 100)

  def create(self, validated_data):
    return Movie.objects.create(validated_data)

  def update(self, instance, validated_data):
    instance.movieId = validated_data.get('movieId', instance.movieId)
    instance.title = validated_data.get('title', instance.title)
    instance.genres = validated_data.get('genres', instance.genres)
    instance.save()
    return instance 

## ModelSerialzer
class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ['userId', 'movieId', 'rating', 'timestamp']