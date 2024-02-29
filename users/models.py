from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)  # email will be username
    password = models.CharField(max_length=255)
    username = None  # Django required field

    USERNAME_FIELD = 'email'  # tell django we will be loging in with username
    REQUIRED_FIELDS = []