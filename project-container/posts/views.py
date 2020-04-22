from django.utils import timezone
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from .serializers import PostSerializer
from posts.models import Post


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.filter(publish__lte=timezone.now())
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.filter(publish__lte=timezone.now())
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]



