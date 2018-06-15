from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'femail')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)