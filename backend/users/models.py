from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    """Кастомный юзер"""

    email = models.EmailField(
        unique=True,
        max_length=254
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=False
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ['-id']


class Subscription(models.Model):
    """Подписка на пользователя"""

    author = models.ForeignKey(
        User,
        related_name="authors",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Автор рецепта"
    )
    follower = models.ForeignKey(
        User,
        related_name="followers",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Подписчик автора",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ['-id']
        constraints = (
            UniqueConstraint(
                fields=("author", "follower"),
                name="Нельзя подписаться дважды",
            ),
        )

    def __str__(self):
        return f"Подписка {self.follower.username} на {self.author.username}"
