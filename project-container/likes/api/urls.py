"""Likes API URL Configuration"""

from django.urls import path
from .views import LikeAPIView

urlpatterns = [
    path('', LikeAPIView.as_view(), name='likes-list-api'),
]

