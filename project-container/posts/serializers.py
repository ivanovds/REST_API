from rest_framework.serializers import ModelSerializer, ReadOnlyField
from posts.models import Post


class PostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')  # restricts to override this field via updating

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'publish', ]
