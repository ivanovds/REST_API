"""Posts API URL Configuration

"""


from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    )


urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list-api'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-api-detail'),
]
