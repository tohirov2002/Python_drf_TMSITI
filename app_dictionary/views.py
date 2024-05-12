from rest_framework import viewsets

from .models import DictionaryModel
from .serializers import DictionarySerializers
from .permissions import IsAdminReadOnly
# Create your views here.


class DictionaryView(viewsets.ModelViewSet):
    queryset = DictionaryModel.objects.all()
    serializer_class = DictionarySerializers
    permission_classes = [IsAdminReadOnly]
