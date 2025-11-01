from rest_framework import serializers
from .models import DistrictPerformance


class DistrictPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictPerformance
        fields = '__all__'

