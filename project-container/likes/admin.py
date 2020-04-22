"""Admin interface

The Django admin application can use your models to automatically build a site area
that you can use to create, view, update, and delete records. This can save you
a lot of time during development, making it very easy to test your models
and get a feel for whether you have the right data.
"""


from django.contrib import admin
from .models import (
    Like
)


class PostLikeModelAdmin(admin.ModelAdmin):
    # list_display = ["post", "user", "like", "dislike"]
    # list_filter = ["post"]
    # search_fields = ["post", "user"]

    class Meta:
        model = Like


admin.site.register(Like, PostLikeModelAdmin)
