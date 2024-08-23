from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=2, max_length=1000)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField(min_value=1, max_value=1000)

    class Meta:
        model = Review
        fields = ['text', 'stars', 'movie_id']

    def validate_movie_id(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise ValidationError('Movie not found')
        return value


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=100)
    stars = serializers.IntegerField(min_value=1, max_value=10)
    movie = serializers.IntegerField(min_value=1, max_value=1000)

    def validate_movie(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise ValidationError('Movie not found')
        return value


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj):
        return obj.movie_set.count()

    class Meta:
        model = Director
        fields = [  'id', 'name', 'movies_count']


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=100)



class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = '__all__'


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.DurationField()
    director_id = serializers.IntegerField(min_value=1, max_value=1000)

    def validate_director_id(self, director_id):
        try:
            Director.object.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director_id


class MovieReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title','description', 'duration', 'director', 'reviews']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            sum_reviews = sum(review.stars for review in reviews)
            return sum_reviews / reviews.count()
        return None