from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    first_name = serializers.SlugField(
        max_length=150,
        required=True
    )
    last_name = serializers.SlugField(
        max_length=150,
        required=True
    )

    class Meta:
        model = Recipe
        fields = ("id", "name", )