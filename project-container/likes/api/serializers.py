from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField,
)
from likes.models import (
    Like,
)


# class PostSerializer(ModelSerializer):
#     user = ReadOnlyField(source='user.username')  # restricts to override this field via updating
#
#     class Meta:
#         model = Like
#         fields = []

#
# class PostLikeSerializer(ModelSerializer):
#     user_id = ReadOnlyField(source='user.user_id')
#     set_or_unset = BooleanField()
#
#     class Meta:
#         model = PostLike
#         fields = ['post_id', 'user_id', 'set_or_unset']


