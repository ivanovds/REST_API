from rest_framework.decorators import action
from rest_framework.response import Response
from likes import services
from accounts.api.serializers import UserDetailSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)


class LikeMixin(object):
    """
       Apply this mixin to any view or viewset to add a like-unlike logic.
    """
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(methods=['POST'], detail=True)
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = UserDetailSerializer(fans, many=True)
        return Response(serializer.data)
