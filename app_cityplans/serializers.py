from rest_framework import serializers

from .models import CityPlansCategory,CitySubPlans,CityMinSubPlans


class CityPlansCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = CityPlansCategory
        fields = '__all__'


class CitySubPlansSerializers(serializers.ModelSerializer):
    class Meta:
        model = CitySubPlans
        fields = '__all__'


class CityMinSubPlansSerializers(serializers.ModelSerializer):
    class Meta:
        model = CityMinSubPlans
        fields = '__all__'
