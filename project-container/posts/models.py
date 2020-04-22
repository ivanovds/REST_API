"""Post Models

A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


def upload_location(instance, filename):
    return '/'.join(['post', str(instance.user.id), filename])


class Post(models.Model):
    """Creates a model Post"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field",
                              )
    publish = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    width_field = models.IntegerField(null=True, default=0)
    height_field = models.IntegerField(null=True, default=0)
    likes = GenericRelation(PostLike)

    def get_absolute_url(self):
        return "/posts/%i/" % self.id

    def __str__(self):
        return self.content

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-publish"]


"""
------------------------ Console commands:

from django.contrib.contenttypes.models import ContentType
from posts.models import PostLike, Post
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.create_user(username='testuser', password='testuser')
post = Post.objects.create(content='People are space puppets', publish='2020-4-19', user=user)
post_model_type = ContentType.objects.get_for_model(post)
PostLike.objects.create(content_type=post_model_type, object_id=post.id, user=user)
PostLike.objects.count()



PostLike.objects.first().content_object
post.total_likes
"""