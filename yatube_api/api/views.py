from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Comment, Group, Post, Follow


class PostViewSet(viewsets.ModelViewSet):
    """ВьюСет для Постов."""

    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ВьюСет для Групп."""

    pass


class CommentViewSet(viewsets.ModelViewSet):
    """ВьюСет для Комментариев."""

    pass


class FollowViewSet(viewsets.ModelViewSet):
    """ВьюСет для Подписок."""

    pass
