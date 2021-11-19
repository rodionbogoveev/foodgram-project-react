from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Ingredient(models.Model):
    '''Модель ингредиента.'''
    name = models.CharField(verbose_name='Название',
                            max_length=200,
                            db_index=True,)
    measurement_unit = models.CharField(verbose_name='Единицы измерения',
                                        max_length=200,)

    def __str__(self):
        return f'{self.name} ({self.measurement_unit})'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']


class Tag(models.Model):
    '''Модель тега.'''
    name = models.CharField(verbose_name='Название',
                            max_length=200,)
    color = ColorField(verbose_name='Цвет',
                       max_length=7,
                       default='#ffffff')
    slug = models.SlugField(verbose_name='Слаг',
                            unique=True,)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']


class Recipe(models.Model):
    '''Модель рецепта.'''
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингредиенты',
                                         through='IngredientRecipe',)
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Тег',
                                  through='TagRecipe',)
    image = models.ImageField(verbose_name='Картинка',
                              upload_to='recipes/',)
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               on_delete=models.CASCADE,
                               related_name='recipes',)
    name = models.CharField(verbose_name='Название',
                            max_length=200,)
    text = models.TextField(verbose_name='Описание',)
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления, мин.',
        validators=[MinValueValidator(
                    1, message='Минимальное время приготовления 1 минута')])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']


class IngredientRecipe(models.Model):
    '''Модель количества игредиента для рецепта.'''
    ingredient = models.ForeignKey(Ingredient,
                                   verbose_name='Ингредиент',
                                   on_delete=models.CASCADE,
                                   related_name='ingredient_recipe')
    recipe = models.ForeignKey(Recipe,
                               verbose_name='Рецепт',
                               on_delete=models.CASCADE,
                               related_name='ingredient_recipe')
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(
                    1, message='Минимальное количество ингредиента - 1')])

    def __str__(self):
        return f'Ингредиент - {self.ingredient}, рецепт - {self.recipe}'

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиентов и рецепте'
        constraints = [models.UniqueConstraint(
            fields=['ingredient', 'recipe'],
            name='unique_ingredient_recipe')]


class TagRecipe(models.Model):
    '''Модель тега для рецепта.'''
    tag = models.ForeignKey(Tag,
                            verbose_name='Тег',
                            on_delete=models.CASCADE,)
    recipe = models.ForeignKey(Recipe,
                               verbose_name='Рецепт',
                               on_delete=models.CASCADE,)

    def __str__(self):
        return f'Тег - {self.tag}, рецепт - {self.recipe}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
