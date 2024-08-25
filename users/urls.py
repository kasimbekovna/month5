from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view, name='registration'),
    path('authorization/', views.authorization_api_view, name='authorization'),
    path('confirm/', views.confirmation_api_view, name='confirm'),
]