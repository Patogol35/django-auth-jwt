from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        STAFF = "staff", "Staff"
        USER = "user", "User"

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
