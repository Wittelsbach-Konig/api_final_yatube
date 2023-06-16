from rest_framework import mixins, viewsets


class ListAndCreateModelMixin(viewsets.GenericViewSet,
                              mixins.CreateModelMixin,
                              mixins.ListModelMixin,):
    """
    Кастомный, абстрактный миксин.
    Доступные запросы: GET, POST.
    """

    pass
