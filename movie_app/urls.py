# movie_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<int:id>/', views.MovieItemAPIView.as_view(), name='movie-detail'),
    path('movies/reviews/', views.MovieReviewsListAPIView.as_view(), name='movie-reviews'),
    path('directors/', views.DirectorListAPIView.as_view(), name='director-list'),
    path('directors/<int:id>/', views.DirectorItemAPIView.as_view(), name='director-detail'),
    path('reviews/', views.ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', views.ReviewItemAPIView.as_view(), name='review-detail'),
]
