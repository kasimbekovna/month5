from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Director(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def movie_title(self):
        return self.title

class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)

    def __str__(self):
        return self.text[:50]  # Limiting the length of the string representation
