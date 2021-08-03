from rest_framework import serializers
from .models import APIField


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIField
        field = '__all__'