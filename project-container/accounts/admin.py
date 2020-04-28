"""Admin interface

The Django admin application can use your models to automatically build a site area
that you can use to create, view, update, and delete records. This can save you
a lot of time during development, making it very easy to test your models
and get a feel for whether you have the right data.
"""


from django.contrib import admin
from .models import (
    UserLoginActivityLog,
    UserRequestActivityLog
)


class UserLoginActivityLogAdmin(admin.ModelAdmin):
    list_display = ['login_username', 'login_IP', 'login_datetime', 'status']
    list_filter = ["status"]
    search_fields = ["user", "login_username"]

    class Meta:
        model = UserLoginActivityLog


class UserRequestActivityLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'last_request_datetime', 'request_method', 'path_info']
    search_fields = ["user", "request_method"]

    class Meta:
        model = UserLoginActivityLog


admin.site.register(UserLoginActivityLog, UserLoginActivityLogAdmin)
admin.site.register(UserRequestActivityLog,UserRequestActivityLogAdmin)

