#path: jSchool/jSchool
from django.db import models

class Theaters(models.Model):
    name = models.CharField(unique=True, max_length=100)
    genres = models.CharField(unique=True, max_length=100)
    rating = models.IntegerField(unique=False)
    points = models.IntegerField(unique=False)
    showtimes = models.CharField(unique=True, max_length=50)
    title = models.CharField(unique=True, max_length=50)
    address = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
