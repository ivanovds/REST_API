"""Project URL Configuration


"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token
from project.api.services import api_root
from accounts.api.views import ObtainJWTView


apipatterns = [
    path('', api_root, name='api-root'),
    path('analytics/', include('likes.api.urls'), name='api-analytics'),
    path('users/', include('accounts.api.urls'), name='api-users'),
    path('posts/', include('posts.api.urls'), name='api-posts'),
    path('auth/token/', ObtainJWTView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', refresh_jwt_token, name='token_refresh'),
]

urlpatterns = [
    path('api/', include(apipatterns), name='api'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

