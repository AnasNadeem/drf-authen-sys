from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=155, min_length=5, write_only=True)

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)

  class Meta:
    model = User
    fields = ('first_name','last_name','username', 'email', 'password')


class LoginSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=155, min_length=5, write_only=True)

  class Meta:
    model = User
    fields = ('email', 'username', 'password', 'token')

    read_only_fields = ['token']