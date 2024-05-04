from django.db import models


# Create your models here.
class Puzzle(models.Model):
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)
    dynasty = models.CharField(max_length=10)
    content = models.CharField(max_length=255)
    keyword = models.CharField(max_length=10)


class Keywords(models.Model):
    name = models.CharField(max_length=10)
