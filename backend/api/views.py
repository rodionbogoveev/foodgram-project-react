from django.shortcuts import get_object_or_404
from recipes.models import Favorite, Ingredient, Recipe, ShoppingCart, Tag
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import AuthorOrReadOnly
from .serializers import (IngredientSerializer, LowerRecipeSerializer,
                          RecipeSerializer, TagSerializer)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            return (AuthorOrReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get', 'delete'],
            permission_classes=[permissions.IsAuthenticated])
    def favorite(self, request, pk):
        if request.method == 'GET':
            return self.add_recipe(Favorite, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_recipe(Favorite, request.user, pk)

    @action(detail=True, methods=['get', 'delete'],
            permission_classes=[permissions.IsAuthenticated])
    def shopping_cart(self, request, pk):
        if request.method == 'GET':
            return self.add_recipe(ShoppingCart, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_recipe(ShoppingCart, request.user, pk)

    def add_recipe(self, model, user, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if model.objects.filter(user=user, recipe=recipe).exists():
            if model.__name__ == 'Favorite':
                return Response(
                    {'errors': 'Рецепт уже есть в избранном.'},
                    status=status.HTTP_400_BAD_REQUEST)
            elif model.__name__ == 'ShoppingCart':
                return Response(
                    {'errors': 'Рецепт уже есть в списке покупок.'},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            model.objects.create(user=user, recipe=recipe)
            serializer = LowerRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_recipe(self, model, user, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if model.objects.filter(user=user, recipe=recipe).exists():
            model.objects.filter(user=user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            if model.__name__ == 'Favorite':
                return Response(
                    {'errors': 'Рецепта нет в избранном.'},
                    status=status.HTTP_400_BAD_REQUEST)
            elif model.__name__ == 'ShoppingCart':
                return Response(
                    {'errors': 'Рецепта нет в списке покупок.'},
                    status=status.HTTP_400_BAD_REQUEST)
