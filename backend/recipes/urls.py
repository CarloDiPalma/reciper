from django.urls import include, path
from rest_framework import routers

from .views import RecipeViewSet, IngredientViewSet, TagViewSet

app_name = 'recipes'

router_v1 = routers.DefaultRouter()
router_v1.register('recipes', RecipeViewSet)
router_v1.register('ingredients', IngredientViewSet)
router_v1.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
