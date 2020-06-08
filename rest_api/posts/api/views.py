from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import Throttled
from likes.api.mixins import LikeMixin
from .serializers import PostSerializer
from posts.models import Post
from rest_api.api.api_settings import env


class PostViewSet(LikeMixin, ModelViewSet):
    """API Post ViewSet that provides all basic methods.

    Endpoint allows you to:
    * get all posts: GET ../api/posts/
    * create new post: POST ../api/posts/
    * get particular post by id: GET ../api/posts/{post_id}/
    * get information about users who liked this post: GET ../api/posts/{post_id}/likes/
    * like this post: POST ../api/posts/{post_id}/likes/
    * unlike this already liked post: DELETE ../api/posts/{post_id}/likes/

    POST and DELETE methods are allowed only for authenticated users.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post_count = Post.objects.filter(user=self.request.user).count()
        if post_count >= env('MAX_POSTS_PER_USER'):
            msg = "You have reached the limit of posts per user."
            raise Throttled(wait=None, detail=msg, code=None)
        else:
            serializer.save(user=self.request.user)

