from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("api/", include("users.urls")),
    path("api/", include("recipes.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("redoc/", TemplateView.as_view(template_name="redoc.html"), name="redoc"),
]
