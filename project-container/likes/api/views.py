from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    DateFilter,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from django.db.models.functions import TruncDay
from django.db.models import Count, DateField
from rest_framework.generics import ListAPIView

from .serializers import LikeSerializer
from likes.models import Like


class LikeFilter(FilterSet):
    date_from = DateFilter(field_name='timestamp', lookup_expr='date__gte')
    date_to = DateFilter(field_name='timestamp', lookup_expr='date__lte')

    class Meta:
        model = Like
        fields = ['date_from', 'date_to']


class LikeAPIView(ListAPIView):
    """
      Return a list of all likes were made up to now, or
      return an analytics with amount of likes from date_from to date_to.

      Example url/api/analytics/?date_from=2020-02-02&date_to=2020-02-15
    """
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeFilter

    likes_per_day = Like.objects.annotate(day=TruncDay('timestamp', output_field=DateField()),)\
        .values('day').annotate(likes=Count('id'))
    for like in likes_per_day:
        print(like['day'], like['likes'])
    print(likes_per_day)
    print("-----")
    # queryset = likes_per_day
    queryset = Like.objects.all()
    print(queryset)

