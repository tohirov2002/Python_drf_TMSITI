from rest_framework import viewsets

# Create your views here.
from .models import DocumentTypes, ElectronicFond
from .serializers import DocumentTypesSerializers, ElectronicFondSerializers
from .permission import IsAdminReadOnly


class DocumentTypesView(viewsets.ModelViewSet):
    queryset = DocumentTypes.objects.all()
    serializer_class = DocumentTypesSerializers
    permission_classes = [IsAdminReadOnly]


class ElectronicFondView(viewsets.ModelViewSet):
    queryset = ElectronicFond.objects.all()
    serializer_class = ElectronicFondSerializers
    permission_classes = [IsAdminReadOnly]

