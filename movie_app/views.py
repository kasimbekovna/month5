from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ( DirectorSerializer, MovieSerializer, ReviewSerializer,
    MovieReviewsSerializer, MovieValidateSerializer,
    DirectorValidateSerializer, ReviewValidateSerializer)
from .models import Director, Movie, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def post(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            director = Director.objects.create(name=name)
            return Response(data={'director_id': director.id, 'name': director.name}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class DirectorItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            duration = serializer.validated_data.get('duration')
            director_id = serializer.validated_data.get('director_id')
            movie = Movie.objects.create(
                title=title,
                description=description,
                duration=duration,
                director_id=director_id,
            )
            return Response(data={'movie_id': movie.id, 'title': movie.title, 'description': movie.description},
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class MovieItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

class MovieReviewsListAPIView(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        if movie_id is None:
            return Review.objects.all()
        return Review.objects.filter(movie_id=movie_id)


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            stars = serializer.validated_data.get('stars')
            movie_id = serializer.validated_data.get('movie_id')
            review = Review.objects.create(
                text=text,
                stars=stars,
                movie_id=movie_id,
            )
            return Response(data={'movie_id': movie_id, 'text': review.text, 'stars': review.stars},
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class ReviewItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'




# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         data = Director.objects.all()
#         list_ = DirectorSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # автоматически сохранит объект
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = DirectorSerializer(director).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = DirectorValidateSerializer(director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         data = Movie.objects.all()
#         list_ = MovieSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # автоматически сохранит объект
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
# #
# #
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = MovieSerializer(movie).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         data = Review.objects.all()
#         list_ = ReviewSerializer(data, many=True).data
#         return Response(data=list_)
#
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # автоматически сохранит объект
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = ReviewSerializer(review).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
#
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)