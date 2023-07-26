from django.contrib import admin

from .models import Tag, Recipe, Ingredient


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'name', 'image', 'cooking_time')
    list_editable = ('text',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'measurement_unit')
    list_display_links = ('name',)
    list_editable = ('measurement_unit',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'