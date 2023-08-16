from django.contrib import admin
from django.contrib.admin import TabularInline, display

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Tag)


class IngredientInline(TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "slug")
    empty_value_display = "-пусто-"
    search_fields = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "name", "image",
                    "cooking_time", "in_favorites_count")
    list_editable = ("text",)
    search_fields = ("name",)
    list_filter = ["name", "author", "tags__name"]
    empty_value_display = "-пусто-"
    inlines = (IngredientInline,)

    @display(description='Количество в избранных')
    def in_favorites_count(self, obj):
        return obj.favorite_set.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "measurement_unit")
    list_display_links = ("name",)
    list_editable = ("measurement_unit",)
    list_filter = ["name"]
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "amount")
    search_fields = ("ingredient",)
    empty_value_display = "-пусто-"


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user")
    search_fields = ("recipe",)
    empty_value_display = "-пусто-"


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user")
    search_fields = ("recipe",)
    empty_value_display = "-пусто-"
