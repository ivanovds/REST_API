"""Application configuration objects store metadata for an application
This file is created to help the user include any application configuration
for the app. Using this, you can configure some of the attributes of the application.
"""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
