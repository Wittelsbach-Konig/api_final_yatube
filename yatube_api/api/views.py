from django.shortcuts import get_object_or_404
from rest_framework import (viewsets,
                            filters,
                            mixins,
                            permissions)
from rest_framework.pagination import LimitOffsetPagination

from posts.models import (Group,
                          Post)
from .serializers import (PostSerializer,
                          CommentSerializer,
                          GroupSerializer,
                          FollowSerializer)
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ВьюСет для Постов."""

    queryset = Post.objects.select_related('group', 'author').all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ВьюСет для Групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """ВьюСет для Комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_post(self) -> Post:
        post = get_object_or_404(
            Post.objects.select_related('group', 'author'),
            id=self.kwargs.get('post_id')
        )
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    ):
    """ВьюСет для Подписок."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
