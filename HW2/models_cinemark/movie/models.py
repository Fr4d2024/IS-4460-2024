from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, blank=True)
    director = models.CharField(max_length=100,blank=True)
    release_year = models.CharField(max_length=50,blank=True)
    budget = models.CharField(max_length=50,blank=True)
    runtime = models.CharField(max_length=50,blank=True)
    rating = models.CharField(max_length=50,blank=True)
    genre = models.CharField(max_length=50,blank=True)


class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=100,blank=True)

class Role(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=False)
    role = models.CharField(max_length=50, null=False)



# Create your models here.