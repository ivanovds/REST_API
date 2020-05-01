"""Admin interface"""


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

