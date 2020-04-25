"""Posts API URL Configuration

"""

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet


urlpatterns = [
    path('', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list-api'),
    path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-detail-api'),
    path('<int:pk>/likes/', PostViewSet.as_view({
        'get': 'fans',
        'post': 'like',
        'delete': 'unlike'}),
         name='post-fans-api'),
]

# router = DefaultRouter()
# router.register(r'', PostViewSet)
#
# urlpatterns = router.urls
