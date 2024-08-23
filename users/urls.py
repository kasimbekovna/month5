from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name='register'),
    path('authorization/', views.AuthorizationAPIView.as_view(), name='authorize'),
    path('confirm/', views.ConfirmationAPIView.as_view(), name='confirm'),
]