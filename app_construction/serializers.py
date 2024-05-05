from rest_framework import serializers
from .models import NewsModel, AdsModel


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsModel
        fields = '__all__'
