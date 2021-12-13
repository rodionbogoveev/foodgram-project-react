from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag, TagRecipe,)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class TagRecipeInline(admin.TabularInline):
    model = TagRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline, TagRecipeInline)
    list_display = ('id', 'author', 'name', 'favorite_count')
    list_filter = ('author', 'name', 'tags')
    ordering = ('-id',)

    def favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    favorite_count.short_description = 'Количество добавлений в избранное'


class IngredientRecipeIAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    list_filter = ('recipe',)


class IngredientIAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')


class TagRecipeAdmin(admin.ModelAdmin):
    list_display = ('tag', 'recipe')
    list_filter = ('tag', 'recipe')


class TagAdmin(admin.ModelAdmin):
    inlines = (TagRecipeInline,)
    list_display = ('name', 'slug')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')


admin.site.register(Ingredient, IngredientIAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeIAdmin)
admin.site.register(TagRecipe, TagRecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
