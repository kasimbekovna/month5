from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializer,
                          MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer)
from .models import Director, Movie, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


# from rest_framework.pagination import PageNumberPagination


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    # pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        name = request.validated_data.get('name')
        director = Director.object.create(name=name)
        return Response(data={'director_id': director.id, 'name': director.name}, status=status.HTTP_201_CREATED)


class DirectorItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        title = request.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.object.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )
        return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description},
                        status=status.HTTP_201_CREATED)


class MovieItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class MovieReviewsListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        data = Movie.oblects.all()
        list_ = MovieReviewsSerializer(data, many=True).data
        return Response(data=list_)


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        text = request.validated_data.get('text')
        movie_id = request.validated_data.get('movie_id')

        review = Review.object.creare(
            text=text,
            movie_id=movie_id,
        )
        return Response(data={'movie_id': movie_id, 'text': review.text},
                        status=status.HTTP_201_CREATED)


class ReviewItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'