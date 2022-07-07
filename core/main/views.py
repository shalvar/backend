from rest_framework.viewsets import ModelViewSet
from main.serializers import MainSerializer
from main.models import Main

class MainViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
