"""Admin interface

The Django admin application can use your models to automatically build a site area
that you can use to create, view, update, and delete records. This can save you
a lot of time during development, making it very easy to test your models
and get a feel for whether you have the right data.
"""


from django.contrib import admin
from .models import Like


class PostLikeModelAdmin(admin.ModelAdmin):
    list_display = ["user", "content_type", "object_id"]
    list_filter = ["object_id", "content_type"]
    search_fields = ["user", "object_id"]

    class Meta:
        model = Like


admin.site.register(Like, PostLikeModelAdmin)
