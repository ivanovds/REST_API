
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from accounts.api.serializers import UserDetailSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    """API uses JSON Web Token authentication.

    Using this API you can:
    * Create account
    * Create a post with text content
    * Like any posts
    * Unlike posts, you liked before
    * Get all posts or one of them
    * Get all users or one of them with activity information
    * Get analytics about how many likes were made
    * Read API bot configuration
    """
    return Response({
        'users': reverse('user-list-api', request=request, format=format),
        'posts': reverse('post-list-api', request=request, format=format),
        'analytics': reverse('likes-list-api', request=request, format=format),
        'get-token': reverse('token_obtain_pair', request=request, format=format),
        'refresh-token': reverse('token_refresh', request=request, format=format),
        'bot-config': reverse('api-config', request=request, format=format),
    })


def jwt_response_payload_handler(token, user=None, request=None, format=None):
    """Overrides default jwt_response_payload_handler."""
    return {
        'token': token,
        'refresh_token_url': reverse('token_refresh', request=request, format=format),
        'user': UserDetailSerializer(user, context={'request': request}).data
    }


@api_view(['GET'])
@permission_classes([AllowAny])
def api_config(request):
    """API configuration for bots."""
    return Response({
        # 'number_of_users': 15,
        'number_of_users': 2,
        # 'max_posts_per_user': 10,
        'max_posts_per_user': 2,
        # 'max_likes_per_user': 20,
        'max_likes_per_user': 3,
        'users_url': 'http://127.0.0.1:8000/api/users/',
        'posts_url': 'http://127.0.0.1:8000/api/posts/',
        'get_token_url': 'http://127.0.0.1:8000/api/auth/token/',
        'refresh_token_url': 'http://127.0.0.1:8000/api/auth/token/refresh/',
        'analytics_url': 'http://127.0.0.1:8000/api/analytics/',
    })


