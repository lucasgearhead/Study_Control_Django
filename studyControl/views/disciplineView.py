from rest_framework import generics
from ..models.disciplineModel import DisciplineModel
from ..serializers.disciplineSerializer import DisciplineModelSerializer


class DisciplineModelList(generics.ListCreateAPIView):
    queryset = DisciplineModel.objects.all()
    serializer_class = DisciplineModelSerializer

class DisciplineModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplineModel.objects.all()
    serializer_class = DisciplineModelSerializer