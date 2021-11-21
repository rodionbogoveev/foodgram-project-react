from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='Адрес электронной почты',
                              max_length=254,
                              unique=True,)
    username = models.CharField(verbose_name='Юзернейм',
                                max_length=150,
                                unique=True,)
    first_name = models.CharField(verbose_name='Имя',
                                  max_length=150,)
    last_name = models.CharField(verbose_name='Фамилия',
                                 max_length=150,)
    password = models.CharField(verbose_name='Пароль',
                                max_length=150,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Follow(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Автор',
                             on_delete=models.CASCADE,
                             related_name='follow_author')
    follower = models.ForeignKey(User,
                                 verbose_name='Подписчик',
                                 on_delete=models.CASCADE,
                                 related_name='follower')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Автор и подписчик'
        verbose_name_plural = 'Авторы и подписчики'
        constraints = [models.UniqueConstraint(
            fields=['user', 'follower'],
            name='unique_user_follower')]

