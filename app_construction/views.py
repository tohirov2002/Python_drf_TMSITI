from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from .models import NewsModel, AdsModel, Category,Specialty,Masters,Leadership,ComponentCategory, Component, Standards
from .serializers import (
    NewsSerializer,
    AdsSerializer,
    CategorySerializers,
    SpecialtySerializers,
    MastersSerializers,
    LeadershipSerializers,
    CnCategorySerializers,
    ComponentSerializers,
    StandardsListSerializers,
    )

from .permissions import IsAdminReadOnly


class NewsView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminReadOnly]


class AdsView(viewsets.ModelViewSet):
    queryset = AdsModel.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAdminReadOnly]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminReadOnly]


class SpecialtyView(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializers
    permission_classes = [IsAdminReadOnly]


class MastersView(viewsets.ModelViewSet):
    queryset = Masters.objects.all()
    serializer_class = MastersSerializers
    permission_classes = [IsAdminReadOnly]


class LeadershipView(viewsets.ModelViewSet):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializers
    permission_classes = [IsAdminReadOnly]


class CnCategoryView(viewsets.ModelViewSet):
    queryset = ComponentCategory.objects.all()
    serializer_class = CnCategorySerializers
    permission_classes = [IsAdminReadOnly]


class ComponentView(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializers
    permission_classes = [IsAdminReadOnly]


class StandardListView(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    serializer_class = StandardsListSerializers
    permission_classes = [IsAdminReadOnly]
