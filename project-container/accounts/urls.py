"""User API URL Configuration

"""


from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserDetailAPIView,
    )


urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-api'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-api-detail'),

]
