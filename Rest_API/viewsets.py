# from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class APIViewset(viewsets.ModelViewSet):
    queryset = models.APIField.objects.all()

    serializer_class = serializers.ApiSerializer

# Create your views here.
