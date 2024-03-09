from django.db import models

class Movies(models.Model):
    movie_id = models.int
    description = models.CharField(max_length=300)
# Create your models here.
