from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=254
    )

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User