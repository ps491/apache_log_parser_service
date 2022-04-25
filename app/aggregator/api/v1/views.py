import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import LogSerializer
from ...models import Log


class CustomLogFilter(django_filters.FilterSet):
    min_time = django_filters.DateTimeFilter(field_name="time", lookup_expr='gte',)
    max_time = django_filters.DateTimeFilter(field_name="time", lookup_expr='lte', )

    class Meta:
        model = Log
        fields = ['ip', 'method', 'status', 'min_time', 'max_time']


class LogListView(ListAPIView):
    """
    Log list

    Filter example:
        method: GET
        status: 200
        max_time: 2020-12-19T13:14:26Z
        min_time: 2020-12-19T13:14:26Z
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CustomLogFilter
    permission_classes = (IsAuthenticated,)


class LogCreate(CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

