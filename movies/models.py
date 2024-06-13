from django.db import models

class Genre(models.Model):
    name = models.charField(max_length = 255)

class Movie(models.model):
    name = models.CharField(max_length = 200)
    