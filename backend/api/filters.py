from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe


class RecipeFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name='author__id'
    )
    tags = filters.CharFilter(
        field_name='tags__slug'
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags']


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'
