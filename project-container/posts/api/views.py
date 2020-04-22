from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from .serializers import (
    PostSerializer,
)
from posts.models import (
    Post,
)


class PostViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(publish__lte=timezone.now())



