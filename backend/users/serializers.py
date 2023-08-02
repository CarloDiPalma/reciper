from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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
    is_subscribed = SerializerMethodField(
        read_only=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("email", "id", "username", "first_name",
                  "last_name", "is_subscribed", "password")

    def get_is_subscribed(self, obj):
        pass
