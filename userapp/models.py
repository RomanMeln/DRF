from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name='псевдоним', max_length=64),
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    date_joined = models.DateTimeField(verbose_name='регистрация', auto_now_add=True)
    email = models.EmailField(verbose_name='электронная почта', unique=True)







