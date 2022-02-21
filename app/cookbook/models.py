from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    '''Продукт'''

    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название продукта',
    )

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()

    class Meta:
        app_label = "cookbook"
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    '''Рецепт'''

    title = models.CharField(
        max_length=100,
        verbose_name='Название рецепта',
    )
    description = models.TextField(
        max_length=10000,
        verbose_name='Описание рецепта',
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "cookbook"
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Unit(models.Model):
    '''Единица измерения'''

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Единица измерения',
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "cookbook"
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Ingredient(models.Model):
    '''Ингредиент в рецепте'''

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='Рецепт',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        verbose_name='Единица измерения',
    )
    quantity = models.FloatField(
        validators=[MinValueValidator(0.01)],
        verbose_name='Количество продукта',
    )

    def __str__(self):
        return 'Ингредиент'

    class Meta:
        app_label = "cookbook"
        verbose_name = "Ингредиент в рецепте"
        verbose_name_plural = "Ингредиенты в рецепте"
