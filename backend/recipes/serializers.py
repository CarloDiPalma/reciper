import base64

from django.core.files.base import ContentFile
from django.db.models import F
from rest_framework import serializers
from rest_framework.fields import (IntegerField, SerializerMethodField,
                                   CurrentUserDefault)
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
    ingredients = SerializerMethodField(method_name='get_ingredients')
    image = Base64ImageField()
    is_favorited = SerializerMethodField(
        method_name='get_is_favorited',
        read_only=True
    )
    is_in_shopping_cart = SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients', 'is_favorited',
                  'is_in_shopping_cart', 'name', 'image', 'text',
                  'cooking_time')

    def get_ingredients(self, recipe):
        ingredients = recipe.ingredients.values(
            'id',
            'name',
            'measurement_unit',
            amount=F('recipeingredient__amount')
        )
        return ingredients

    def get_is_favorited(self, recipe):
        if self.context.get('request').method == 'POST':
            return False
        user = self.context.get('request').user

        if user.is_anonymous:
            return False
        return user.favorite_set.filter(recipe=recipe).exists()

    def get_is_in_shopping_cart(self, recipe):
        if self.context.get('request').method == 'POST':
            return False
        user = self.context.get('request').user

        if user.is_anonymous:
            return False
        return user.shoppingcart_set.filter(recipe=recipe).exists()


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

    def update(self, recipe, validated_data):
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredients')
        instance = super().update(recipe, validated_data)
        if tags:
            instance.tags.clear()
            instance.tags.set(tags)
        if ingredients:
            instance.ingredients.clear()

            RecipeIngredient.objects.bulk_create(
                [RecipeIngredient(
                    ingredient=Ingredient.objects.get(id=ingredient['id']),
                    recipe=recipe,
                    amount=ingredient.get('amount')
                ) for ingredient in ingredients]
            )

        instance.save()
        return instance

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeReadSerializer(instance, context=context).data
