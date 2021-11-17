from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Юзернейм',
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',
                       'last_name', 'password']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        # constraints = [
        #     models.CheckConstraint(
        #         check=~models.Q(username__iexact="me"),
        #         name="username_is_not_me"
        #     )
        # ]
