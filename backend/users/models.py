from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser):
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

    # objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ['-id']
