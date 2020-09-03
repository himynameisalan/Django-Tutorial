from django.db import models

# Create your models here.

class Movie(models.Model):
  movieId = models.CharField(max_length = 100)
  title = models.CharField(max_length = 100)
  genres = models.CharField(max_length = 100)

  def __str__(self):
    return self.title

class Rating(models.Model):
  userId = models.CharField(max_length = 100)
  movieId = models.CharField(max_length = 100)
  rating = models.CharField(max_length = 100)
  timestamp = models.CharField(max_length = 100)

  def __str__(self):
    return self.rating 