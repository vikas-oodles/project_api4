from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserModelSerializer, UserLoginSerializer
# Create your views here.
UserModel = get_user_model()

class UserApiView(ListCreateAPIView):
    
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated,]

class UserLoginView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserLoginSerializer

    def post(self,request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.data, status=status.HTTP_400_BAD_REQUEST)

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