from django.contrib import admin
from .models import (Ingredient, Tag, Recipe, IngredientRecipe, TagRecipe,
                     Favorite, ShoppingCart)


class RecipeIngredientInline(admin.TabularInline):
    """
    Для отображения в админке поля ManyToMany ингредиентов в рецепте c through.
    """
    model = IngredientRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)
    list_display = ('author', 'name')
    list_filter = ('author', 'name', 'tags')
    empty_value_display = "-пусто-"


admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(TagRecipe)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
