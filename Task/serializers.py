from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'password', 'email', 'is_staff', 'is_superuser', 'is_active',  'date_joined', 'last_login']

    def create(self, validated_data):
        user = User.objects.create(
        email = validated_data['email'],
        username = validated_data['username'],
        password = make_password(validated_data['password']),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
