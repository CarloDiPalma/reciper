from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=70
    )
    color = models.CharField(
        max_length=7
    )
    slug = models.SlugField(
        max_length=50
    )


class Ingredient(models.Model):
    name = models.CharField(
        max_length=70
    )
    measurement_unit = models.CharField(
        max_length=10,
        verbose_name='Единицы измерения'
    )


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=200
    )
    text = models.TextField(
        blank=True
    )
    image = models.ImageField(
        upload_to=None
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message='Минимум один час')
        ]
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты'
    )

    class RecipeIngredient(models.Model):
        recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            verbose_name='Рецепт',
        )
        ingredient = models.ForeignKey(
            Ingredient,
            on_delete=models.CASCADE,
            verbose_name='Ингредиент',
        )
        amount = models.PositiveSmallIntegerField(
            verbose_name='Количество',
            validators=[
                MinValueValidator(1, message='Минимум 1')
            ]
        )

