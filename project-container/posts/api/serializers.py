from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField,
    SerializerMethodField,
)
from posts.models import Post
from likes import services


class PostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')  # restricts to override this field via updating
    is_fan = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'image',
            'publish',
            'total_likes',
            'is_fan'
        ]

    def get_is_fan(self, obj) -> bool:

        user = self.context.get('request').user
        return services.is_fan(obj, user)
