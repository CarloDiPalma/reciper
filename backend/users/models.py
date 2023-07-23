from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
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

    class Meta:
        ordering = ['-id']
