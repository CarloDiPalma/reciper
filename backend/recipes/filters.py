from django_filters.rest_framework import (
    AllValuesMultipleFilter,
    BooleanFilter,
    FilterSet,
    filters,
)

from .models import Ingredient, Recipe


class RecipeFilter(FilterSet):
    is_favorited = BooleanFilter(method="get_is_favorited")
    is_in_shopping_cart = BooleanFilter(method="get_is_in_shopping_cart")
    tags = AllValuesMultipleFilter(field_name="tags__slug")

    class Meta:
        model = Recipe
        fields = ("author",)

    def get_is_favorited(self, queryset, name, value):
        if not value:
            return queryset
        favorites = self.request.user.favorite_set.all()
        return queryset.filter(pk__in=(favorite.recipe.pk for favorite in favorites))

    def get_is_in_shopping_cart(self, queryset, name, value):
        if not value:
            return queryset
        cart_recipes = self.request.user.shoppingcart_set.all()
        return queryset.filter(
            pk__in=(cart_recipe.recipe.pk for cart_recipe in cart_recipes)
        )


class IngredientFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="startswith")

    class Meta:
        model = Ingredient
        fields = ["name"]
