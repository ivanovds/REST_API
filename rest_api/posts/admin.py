"""Admin interface"""

from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "content", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["user", "content"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)

