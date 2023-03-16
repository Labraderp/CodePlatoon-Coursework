from django.db import models

# Create your models here.
class Role(models.Model):
    role_title = models.CharField(max_length=50)

class Movie(models.Model):
    movie_title = models.CharField(max_length=50)

class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    movies = models.ManyToOneRel(Movie)
    role = models.OneToOneField(Role)