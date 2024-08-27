from django.urls import path
from . import views

urlpatterns = [
    # path('registration/', views.registration_api_view, name='registration'),
    path('registration/',views.RegistrationAPIView.as_view()),
#     path('authorization/', views.authorization_api_view, name='authorization'),
    path('authorization/',views.AuthorizationAPIView.as_view()),
#     path('confirm/', views.confirmation_api_view, name='confirm'),
    path('confirm/',views.ConfirmationAPIView.as_view()),
 ]