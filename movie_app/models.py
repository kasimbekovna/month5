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

    @property
    def rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_stars = sum(review.stars for review in reviews)
            average_rating = total_stars / reviews.count()
            return round(average_rating, 1)  # Округление до одного знака после запятой
        return 0  # Возвращаем 0, если нет отзывов

STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    stars = models.PositiveIntegerField(choices=STAR_CHOICES,default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)

    def __str__(self):
        return self.text[:50]
