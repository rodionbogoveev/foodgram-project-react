from django.contrib import admin

from users.models import Follow

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag, TagRecipe)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class TagRecipeInline(admin.TabularInline):
    model = TagRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline, TagRecipeInline)
    list_display = ('author', 'name')
    list_filter = ('author', 'tags')


class IngredientRecipeIAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    list_filter = ('recipe',)


class IngredientIAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')


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


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'follower')
    list_filter = ('user', 'follower')


admin.site.register(Ingredient, IngredientIAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeIAdmin)
admin.site.register(TagRecipe, TagRecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Follow, FollowAdmin)
