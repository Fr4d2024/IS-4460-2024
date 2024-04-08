from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
# Create your models here.
