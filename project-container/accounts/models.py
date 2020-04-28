"""Account Models

A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""

from django.db import models
from django.conf import settings


class UserLoginActivityLog(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'
    LOGIN_STATUS = [(SUCCESS, 'Success'),
                    (FAILED, 'Failed')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='login_activity', on_delete=models.CASCADE, null=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)

    def __str__(self):
        return f' login_status: {self.status}  |  login_datetime: {self.login_datetime}'


class UserRequestActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_activity',
                             on_delete=models.CASCADE, null=False)
    last_request_datetime = models.DateTimeField(auto_now=True)
    request_method = models.CharField(max_length=20, null=True, blank=True)
    path_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'last_request_datetime: {self.last_request_datetime}  |  ' \
               f'request_method: {self.request_method}  |  ' \
               f'path_info: {self.path_info}'
