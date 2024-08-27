from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer, ConfirmationSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import ConfirmationCode
from rest_framework.views import APIView


# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     user = User.objects.create_user(username=username, password=password)
#     return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['POST'])
# def confirmation_api_view(request):
#     if request.method == 'POST':
#         serializer = ConfirmationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data={'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def authorization_api_view(request):
#     if request.method == 'POST':
#         serializer = UserAuthSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         username = serializer.validated_data.get('username')
#         password = serializer.validated_data.get('password')
#
#         user = User(username=username, password=password)
#         if user is not None:
#             token = Token.objects.get(user=user)
#             return Response(data={'key': token.key})
#         return Response(status=status.HTTP_401_UNAUTHORIZED,
#                         data={'error': 'User credentials are wrong!'})
class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        confirmation_code = user.confirmation_code.code

        return Response(data={'user_id': user.id, 'confirmation_code': confirmation_code},
                        status=status.HTTP_201_CREATED)


class ConfirmationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)


class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'User credentials are wrong!'})