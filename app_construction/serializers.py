from rest_framework import serializers
from .models import (
    NewsModel,
    AdsModel,
    Category,
    Specialty,
    Masters,
    Leadership,
    ComponentCategory,
    Component,
    Standards
    )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsModel
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SpecialtySerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class MastersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = '__all__'


class LeadershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class CnCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ComponentCategory
        fields = '__all__'


class ComponentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class StandardsListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Standards
        fields = '__all__'


