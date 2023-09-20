from rest_framework import generics
from ..models.studentModel import StudentModel
from ..serializers.studentSerializer import StudentModelSerializer


class StudentModelList(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

class StudentModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer