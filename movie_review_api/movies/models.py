from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ChaeField(max_length=255)
    release_date = models.DateField()

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    movie = modles.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
