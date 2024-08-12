from rest_framework.response import Response
from rest_framework import status
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializer,
                          MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer)
from .models import Director, Movie, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def post(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'director_id': director.id, 'name': director.name}, status=status.HTTP_201_CREATED)

class DirectorItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class MovieListAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )
        return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description},
                        status=status.HTTP_201_CREATED)

class MovieItemAPIView(RetrieveUpdateDestroyAPIView):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

class MovieReviewsListAPIView(ListAPIView):
    # queryset = Movie.objects.all()
    serializer_class = MovieReviewsSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie')

        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        return Response(data={'movie_id': movie_id, 'text': review.text, 'stars': review.stars},
                        status=status.HTTP_201_CREATED)

class ReviewItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
