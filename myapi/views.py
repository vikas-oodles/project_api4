from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserModelSerializer
from django.contrib.auth import get_user_model
# Create your views here.
UserModel = get_user_model()

class UserRegistrationApiView(GenericAPIView):
    serializer_class = UserModelSerializer

    def post(self, request, format='json'):
        serializer = UserModelSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()

            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token']=token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)