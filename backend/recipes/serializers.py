import base64

from django.core.files.base import ContentFile
from django.db.models import F
from rest_framework import serializers
from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.generics import get_object_or_404
from rest_framework.relations import PrimaryKeyRelatedField
from users.serializers import UserCreateSerializer

from .models import Ingredient, Recipe, Tag, RecipeIngredient


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
        many=True,
        read_only=True
    )
    author = UserCreateSerializer(read_only=True)
    ingredients = SerializerMethodField()
    image = Base64ImageField()
    # last_name = serializers.SlugField(
    #     max_length=150,
    #     required=True
    # )

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'name', 'image', 'text', 'cooking_time')

    def get_ingredients(self, recipe):
        ingredients = recipe.ingredients.values(
            'id',
            'name',
            'measurement_unit',
            amount=F('recipeingredient__amount')
        )
        return ingredients


class RecipeIngredientWriteSerializer(serializers.ModelSerializer):
    id = IntegerField(write_only=True)
    amount = IntegerField(write_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'amount')


class RecipeWriteSerializer(serializers.ModelSerializer):
    tags = PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    author = UserCreateSerializer(read_only=True)
    ingredients = RecipeIngredientWriteSerializer(many=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'name', 'image', 'text', 'cooking_time')

    def create(self, validated_data):
        print(validated_data)
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        RecipeIngredient.objects.bulk_create(
            [RecipeIngredient(
                ingredient=Ingredient.objects.get(id=ingredient['id']),
                recipe=recipe,
                amount=ingredient.get('amount')
            ) for ingredient in ingredients]
        )
        return recipe

    def to_representation(self, instance):
        serializer = RecipeReadSerializer(instance)
        return serializer.data
