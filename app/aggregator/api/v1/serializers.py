from rest_framework import serializers

from aggregator.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
