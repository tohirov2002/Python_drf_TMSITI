from rest_framework import serializers

from .models import DocumentTypes, ElectronicFond


class DocumentTypesSerializers(serializers.ModelSerializer):

    class Meta:
        model = DocumentTypes
        fields = '__all__'


class ElectronicFondSerializers(serializers.ModelSerializer):
    class Meta:
        model = ElectronicFond
        fields = '__all__'
