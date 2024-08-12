from django.urls import path
from . import views


urlpatterns = [

    path('', views.MovieListAPIView.as_view()),
    path('<int:id>/', views.MovieItemAPIView.as_view()),

    path('api/v1/movies/reviews', views.MovieReviewsListAPIView.as_view()),
    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:id>', views.DirectorItemAPIView.as_view()),

    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewItemAPIView.as_view()),
]