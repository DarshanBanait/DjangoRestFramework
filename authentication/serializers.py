from rest_framework import serializers
from authentication.models import User
#from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    """ In Django REST Framework, the class Meta is used within serializers to provide metadata about the serializer. This metadata can include information such as which model to use, which fields to include or exclude, and additional options for the serializer’s behavior. """

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 
    # **validated_data, here ** is used to unpack the validated_data dictionary into keyword arguments
        

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

        read_only_fields = ['token']

    """def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token
        }"""