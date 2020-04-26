from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
)
from django.contrib.auth.models import User
from rest_framework.permissions import (
    IsAuthenticated,
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
    permission_classes = [IsAuthenticatedOrWriteOnly]


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer
