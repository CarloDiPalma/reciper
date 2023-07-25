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


class Recipe(models.Models):
    author = models.ForeignKey(
        User,
        verbose_name='Автор'
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

