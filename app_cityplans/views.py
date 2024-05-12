from rest_framework import viewsets

from .models import CityPlansCategory, CitySubPlans, CityMinSubPlans
from .serializers import CityPlansCategorySerializers, CitySubPlansSerializers, CityMinSubPlansSerializers
from .permissions import IsAdminReadOnly


class CityPlansCategoryView(viewsets.ModelViewSet):
    queryset = CityPlansCategory.objects.all()
    serializer_class = CityPlansCategorySerializers
    permission_classes = [IsAdminReadOnly]


class CitySubPlansView(viewsets.ModelViewSet):
    queryset = CitySubPlans.objects.all()
    serializer_class = CitySubPlansSerializers
    permission_classes = [IsAdminReadOnly]


class CityMinPlansView(viewsets.ModelViewSet):
    queryset = CityMinSubPlans.objects.all()
    serializer_class = CityMinSubPlansSerializers
    permission_classes = [IsAdminReadOnly]
