from rest_framework import serializers

from .models import Recipe, Tag, Ingredient
from users.serializers import UserCreateSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class RecipeReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        # many=True,
        required=True,
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


class RecipeWriteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        # many=True,
        required=True,
    )
    author = UserCreateSerializer(
        many=False
    )

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'name', 'image', 'text', 'cooking_time')