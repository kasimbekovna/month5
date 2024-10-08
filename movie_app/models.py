from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)


