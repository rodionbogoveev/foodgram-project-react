from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)
from users.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientRecipeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = IngredientRecipe
        fields = ('id', 'name', 'measurement_unit', 'amount')
        validators = [
            UniqueTogetherValidator(
                queryset=IngredientRecipe.objects.all(),
                fields=['ingredient', 'recipe']
            )
        ]


class LowerRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientRecipeSerializer(
        source='ingredient_recipe',
        many=True,
        read_only=True,
    )
    author = UserSerializer(read_only=True)
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients', 'is_favorited',
                  # 'image'
                  'is_in_shopping_cart', 'name', 'text', 'cooking_time')

    def get_is_favorited(self, obj):
        request = self.context['request']
        user = request.user.pk
        recipe = obj.pk
        return Favorite.objects.filter(user=user, recipe=recipe).exists()

    def get_is_in_shopping_cart(self, obj):
        request = self.context['request']
        user = request.user.pk
        recipe = obj.pk
        return ShoppingCart.objects.filter(user=user, recipe=recipe).exists()

    def validate(self, data):
        tags = self.initial_data.get('tags')
        if not tags:
            raise ValidationError('Укажите хотя бы один тег.')
        if len(tags) != len(set(tags)):
            raise ValidationError('Теги не должны повторяться.')
        for tag in tags:
            get_object_or_404(Tag, pk=tag)
        data['tags'] = tags

        ingredients_list = []
        ingredients = self.initial_data.get('ingredients')
        if not ingredients:
            raise ValidationError('Укажите хотя бы один ингредиент.')
        for ingredient in ingredients:
            get_object_or_404(Ingredient, pk=ingredient['id'])
            if ingredient['amount'] < 1:
                raise ValidationError('Минимальное количество игредиента - 1.')
            if ingredient in ingredients_list:
                raise ValidationError('Ингредиенты не должны повторяться.')
            ingredients_list.append(ingredient)
        data['ingredients'] = ingredients_list

        cooking_time = self.initial_data.get('cooking_time')
        if cooking_time < 1:
            raise ValidationError('Минимальное время приготовления - 1 мин.')
        return data

    def create_ingredients(self, recipe, ingredients):
        for ingredient in ingredients:
            IngredientRecipe.objects.create(
                recipe=recipe,
                ingredient_id=ingredient.get('id'),
                amount=ingredient.get('amount'))

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        self.create_ingredients(recipe, ingredients)
        recipe.tags.set(tags)
        return recipe

    def update(self, request, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.get(pk=request.id)
        recipe.ingredients.clear()
        recipe.tags.set(tags)
        self.create_ingredients(recipe, ingredients)
        return recipe
