from django_filters.rest_framework import filters, FilterSet
from rest_framework.filters import SearchFilter

from recipes.models import Recipe


class RecipeFilter(FilterSet):
    author = filters.CharFilter(
        field_name='author__id'
    )
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug'
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags']


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'
