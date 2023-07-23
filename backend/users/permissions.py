from rest_framework import permissions


class AdminAndSuperUser(permissions.BasePermission):
    """Админ или суперюзер"""

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_admin or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user.is_admin