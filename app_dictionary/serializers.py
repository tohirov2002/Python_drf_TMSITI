from rest_framework import serializers

from .models import DictionaryModel


class DictionarySerializers(serializers.ModelSerializer):

    class Meta:
        model = DictionaryModel
        fields = '__all__'
