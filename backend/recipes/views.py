from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from .models import Recipe, Ingredient, Tag
from .serializers import (RecipeReadSerializer, RecipeWriteSerializer,
                          IngredientSerializer, TagSerializer)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    # permission_classes = (AdminAndSuperUser,)
    # pagination_class = CustomPagination
    # filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'id'
    http_method_names = ['get', 'post', 'patch', 'del']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeReadSerializer
        return RecipeWriteSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'id'
    http_method_names = ['get']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
    http_method_names = ['get']
