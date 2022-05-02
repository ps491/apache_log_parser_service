import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import LogSerializer, LogCreateSerializer
from ...models import Log
from ...services.re_log import re_logs_to_dict


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

    def create(self, request, *args, **kwargs):
        """Получаем лог в виде json.
        Распарсиваем и добавляем в request.data"""
        # проверка лога на формат
        serializer = LogCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # распарсиваем и отдаем в основной сериализатор для сохранения
            d = re_logs_to_dict(serializer.data.get('log'))
            self.request.data.update(d)
            return super().create(request, *args, **kwargs)
        return Response(status=400)
