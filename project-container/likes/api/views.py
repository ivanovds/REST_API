# from django.utils import timezone
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.status import HTTP_400_BAD_REQUEST
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import (
#     IsAuthenticated,
#     AllowAny
# )
# from .serializers import (
#     LikeSerializer,
# )
# from likes.models import (
#     Like,
# )


# class LikeViewSet(ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     serializer_class = LikeSerializer
#     queryset = Like.objects.filter(publish__lte=timezone.now())
#
#
# class LikeDislikeViewSet(ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     queryset = Post.objects.filter(publish__lte=timezone.now())
#     serializer_class = LikeDislikeSerializer
#
#     @action(detail=True, methods=['post'])
#     def set_or_unset_like(self, request, pk=None):
#         serializer = LikeDislikeSerializer(data=request.data)
#         # like_queryset = Like.objects.filter(user=)
#         if serializer.is_valid() and serializer.data['set_or_unset']:
#             print("true!")
#             print(request.user)
#             like_obj = Like(post_id=pk, like=True, dislike=False)
#
#             like_obj.save()
#             return Response({'status': 'Like set.'})
#         else:
#             return Response(serializer.errors,
#                             {'status': 'xxx'})

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


