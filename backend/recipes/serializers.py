from rest_framework import serializers

from .models import Recipe, Tag
from users.serializers import UserCreateSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        many=True,
        required=True,
        # source='tag_set'
    )
    author = UserCreateSerializer(
        many=False
    )
    # last_name = serializers.SlugField(
    #     max_length=150,
    #     required=True
    # )

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'name', 'image', 'text', 'cooking_time')
