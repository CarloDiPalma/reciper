from rest_framework import viewsets

from .models import Recipe, Ingredient, Tag
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = (AdminAndSuperUser,)
    # pagination_class = CustomPagination
    # filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'id'
    http_method_names = ['get', 'post']


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'id'
    http_method_names = ['get', 'post']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
    http_method_names = ['get', 'post']