from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
)
from django.contrib.auth.models import User
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import (
    UserDetailSerializer,
    UserListCreateSerializer,
    JWTSerializer,
)
from .permissions import IsAuthenticatedOrWriteOnly


class UserListCreateAPIView(ListCreateAPIView):
    """Endpoint to get a list of all users or
    to create a new one.

    Username requirements:
    Your username must be unique.

    Password requirements:
    Your password can’t be too similar to your other personal information.
    Your password must contain at least 8 characters.
    Your password can’t be a commonly used password.
    Your password can’t be entirely numeric.
    """

    queryset = User.objects.all()
    serializer_class = UserListCreateSerializer
    # permission_classes = [IsAuthenticatedOrWriteOnly]
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = [IsAuthenticatedOrWriteOnly]
    permission_classes = [AllowAny]


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer
