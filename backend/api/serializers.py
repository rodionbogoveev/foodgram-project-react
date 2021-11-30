from rest_framework import serializers

from recipes.models import Favorite, Ingredient, Tag, TagRecipe, Recipe, ShoppingCart
from users.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class RecipeSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True)
    author = UserSerializer(read_only=True)
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 
            'ingredients',
            # 'image'
            'is_favorited',
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

    # def validate(self, data):
    #     tags = self.initial_data.pop('tags')
    #     for tag in tags:
    #         current_tag = Tag.objects.filter(pk=tag)
    #         print(current_tag)
            # if current_tag:

    def create(self, validated_data):
        # image = validated_data.pop('image')
        print(' ')
        print(validated_data)
        print(' ')
        # tags_data = validated_data.pop('tags')
        # # ingredients_data = validated_data.pop('ingredients')
        # recipe = Recipe.objects.create(**validated_data)
        # self.create_ingredients(ingredients_data, recipe)
        # recipe.tags.set(tags_data)
        # return recipe
