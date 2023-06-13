from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly


class AuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """Класс Разрешений.
    Полный доступ к объекту только у автора."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in SAFE_METHODS
        )
