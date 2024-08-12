from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars', 'movie']


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=100)
    stars = serializers.IntegerField(min_value=1)
    movie = serializers.IntegerField(min_value=1, max_value=1000)


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj):
        return obj.movie_set.count()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = 'id title text category tags reviews'.split()
        # depth = 1


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.DurationField()
    director = serializers.IntegerField(min_value=1, max_value=1000)


    def validate_director_id(self, director_id):
        try:
            Director.object.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director_id


class MovieReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, product):
        reviews = product.reviews.all()
        if reviews:
            sum_reviews = sum(i.stars for i in reviews)
            average = sum_reviews / len(reviews)
            return average
        return None

    class Meta:
        model = Movie
        fields = 'title description duration director reviews average_rating'.split()

