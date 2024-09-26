from django.shortcuts import render
from rest_framework import generics
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status
from django.contrib.auth import authenticate

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        else:

            return response.Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)