from django.shortcuts import render
from rest_framework import generics
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

class AuthUserAPIView(generics.RetrieveAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        user = request.user

        serializer = RegisterSerializer(user)

        return response.Response({'user': serializer.data}, status=status.HTTP_200_OK)

class RegisterAPIView(generics.CreateAPIView):

    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.CreateAPIView):

    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)