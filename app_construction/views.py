from django.shortcuts import render
from rest_framework import viewsets

from .models import NewsModel, AdsModel
from .serializers import NewsSerializer, AdsSerializer
from .permissions import IsAdminReadOnly


class NewsView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminReadOnly]


class AdsView(viewsets.ModelViewSet):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAdminReadOnly]
