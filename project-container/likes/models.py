"""Like Models"""

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Like(models.Model):
    """Creates a  model Like

    Like is based on the ContentType framework built into Django. The ContentType provides a
    GenericForeignKey relationship that creates generic relationships between models.
    For comparison, a regular ForeignKey creates a relationship only with a particular model.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
