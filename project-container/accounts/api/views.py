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
