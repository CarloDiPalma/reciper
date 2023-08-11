from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.author == request.user
