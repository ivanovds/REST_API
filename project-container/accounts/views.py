from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
)

from django.contrib.auth.models import User
from .serializers import (
    UserDetailSerializer,
    UserListCreateSerializer,
)
from rest_framework.permissions import (
    IsAuthenticated,
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

