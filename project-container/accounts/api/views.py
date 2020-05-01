from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
)
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import (
    UserDetailSerializer,
    UserListCreateSerializer,
    JWTSerializer,
)


class UserListCreateAPIView(ListCreateAPIView):
    """This view allows to get a list of all users or
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
    permission_classes = [AllowAny]



class UserDetailAPIView(RetrieveAPIView):
    """Endpoint with user`s detail information."""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class ObtainJWTView(ObtainJSONWebToken):
    """You can use the returned access token to prove authentication for a protected views.

    When this short-lived access token expires, you can use the longer-lived refresh token
    to obtain another access token via 'refresh_token_url'.
    """
    serializer_class = JWTSerializer
