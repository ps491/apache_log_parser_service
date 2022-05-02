from rest_framework import serializers

from aggregator.models import Log
from aggregator.services.re_log import get_re_pattern


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class LogCreateSerializer(serializers.Serializer):

    log = serializers.RegexField(get_re_pattern())

