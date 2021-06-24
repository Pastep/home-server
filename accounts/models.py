from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


def create_path(instance, filename):
    return f"avatars/{instance.username}/{filename}"
class User(AbstractUser):

    username = models.CharField(
        unique=True,
        max_length=200,
        null=False
    )
    email = models.EmailField(
        unique=True,
        null=False
    )
    avatar = models.ImageField(upload_to=create_path, default="avatars/static/default.png")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']