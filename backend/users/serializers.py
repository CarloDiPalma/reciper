from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    first_name = serializers.SlugField(
        max_length=150,
        required=True
    )
    last_name = serializers.SlugField(
        max_length=150,
        required=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("email", "id", "username", "first_name", "last_name", "password")
