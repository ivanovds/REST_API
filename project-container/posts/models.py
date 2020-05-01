"""Post Models"""

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like


def upload_location(instance, filename):
    return '/'.join(['post', str(instance.user.id), filename])


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field",
                              )
    width_field = models.IntegerField(null=True, default=0)
    height_field = models.IntegerField(null=True, default=0)
    likes = GenericRelation(Like)

    def get_absolute_url(self):
        return "/posts/%i/" % self.id

    def __str__(self):
        return self.content

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-timestamp"]
