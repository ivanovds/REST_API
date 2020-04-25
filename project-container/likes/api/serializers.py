from datetime import date
from django.db import models
from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    DateField,
)
from likes.models import Like


class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = [
            'content_type',
            'object_id',
            'user_id',
            'timestamp',
        ]
        extra_kwargs = {
            'content_type': {"read_only": True},
            'object_id': {'read_only': True}
        }
