from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class AuthorOrReadOnly(IsAuthenticated):
    """Класс Разрешений.
    Полный доступ к объекту только у автора."""

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in SAFE_METHODS
        )
