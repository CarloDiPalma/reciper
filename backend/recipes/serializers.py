import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from users.serializers import UserCreateSerializer

from .models import Ingredient, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class RecipeReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        # many=True,
        required=True,
    )
    author = UserCreateSerializer(
        many=False
    )
    image = Base64ImageField()
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
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'name', 'image', 'text', 'cooking_time')

    def create(self, validated_data):
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(validated_data)
