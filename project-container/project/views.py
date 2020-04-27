from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from accounts.api.serializers import UserDetailSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request, format=None):

    return Response({
        'users': reverse('user-list-api', request=request, format=format),
        'posts': reverse('post-list-api', request=request, format=format),
        'analytics': reverse('likes-list-api', request=request, format=format),
    })


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }