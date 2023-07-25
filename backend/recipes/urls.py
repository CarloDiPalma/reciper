from django.urls import include, path
from rest_framework import routers

app_name = 'users'

router_v1 = routers.DefaultRouter()
router_v1.register('recipes', RecipeViewSet)