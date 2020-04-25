"""Likes API URL Configuration

"""

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import LikeAPIView


urlpatterns = [
    path('', LikeAPIView.as_view(), name='likes-list-api'),
]

# router = DefaultRouter()
# router.register(r'', PostViewSet)
#
# urlpatterns = router.urls
