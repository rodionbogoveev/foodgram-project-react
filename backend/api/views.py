from recipes.models import Ingredient, Recipe, Tag
from rest_framework import filters, viewsets

from .serializers import IngredientSerializer, RecipeSerializer, TagSerializer


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

    # def get_serializer_class(self):
    #     if self.action in ('retrieve', 'list'):
    #         return ReadOnlyRecipeSerializer
    #     return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def create(self, request):
    #     data = request.data
    #     new_recipe = Recipe.objects.create(

    #     )