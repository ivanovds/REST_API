"""Application configuration objects store metadata for an application
This file is created to help the user include any application configuration
for the app. Using this, you can configure some of the attributes of the application.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from .signals import log_user_logged_in_success
