from django_filters.rest_framework import (
    FilterSet, BooleanFilter, AllValuesMultipleFilter
)

from .models import Recipe


class RecipeFilter(FilterSet):
    is_favorited = BooleanFilter(method='get_is_favorited')

    class Meta:
        model = Recipe
        fields = ('author',)

    def get_is_favorited(self, queryset, name, value):
        if not value:
            return queryset
        favorites = self.request.user.favorite_set.all()
        return queryset.filter(
            pk__in=(favorite.recipe.pk for favorite in favorites)
        )
