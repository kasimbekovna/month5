# movie_app/urls.py
from django.urls import path
from . import views
from .views import (
    movie_list_api_view,
    movie_detail_api_view,
    director_list_api_view,
    director_detail_api_view,
    review_list_api_view,
    review_detail_api_view
)
urlpatterns = [
    path('', views.MovieListAPIView.as_view()),
    path('movies/', movie_list_api_view, name = 'movie-list-api'),
    path('movies/<int:id>/', movie_detail_api_view, name='movie-detail'),
    path('directors/', director_list_api_view, name = 'director-list'),
    path('directors/<int:id>/', director_detail_api_view, name='director-detail'),
    path('reviews/', review_list_api_view, name = 'review-list'),
    path('reviews/<int:id>/', review_detail_api_view, name='review-detail'),
   ]
