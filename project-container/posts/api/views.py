from django.utils import timezone
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from likes.api.mixins import LikeMixin
from .serializers import PostSerializer
from posts.models import Post


class PostViewSet(LikeMixin, ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(publish__lte=timezone.now())


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):

    return Response({
        'users': reverse('user-list-api', request=request, format=format),
        'posts': reverse('post-list-api', request=request, format=format),
        'analytics': reverse('likes-list-api', request=request, format=format),
    })
