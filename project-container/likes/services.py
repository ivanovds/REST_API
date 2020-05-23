"""likes.services.py - a set of methods used in likes.api.mixins"""

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import Throttled
from .models import Like
from project.api.api_settings import env


def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)

    like_count = Like.objects.filter(user=user).count()
    if like_count >= env('MAX_LIKES_PER_USER'):
        msg = "You have reached the limit of likes per user."
        raise Throttled(wait=None, detail=msg, code=None)
    else:
        like, is_created = Like.objects.get_or_create(
            content_type=obj_type, object_id=obj.id, user=user)
    return like


def remove_like(obj, user):

    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_fan(obj, user) -> bool:

    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()


def get_fans(obj):

    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)