from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from rest_framework import status
from .serializers import MovieSerializer

@api_view(['GET'])
def movies_detail_api_view(request, id):
    movies = Movie.objects.get(id=id)
    data = MovieSerializer(movies).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()

    list_ = MovieSerializer(instance=movies, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


