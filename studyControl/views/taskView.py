from rest_framework import generics
from ..models.taskModel import TaskModel
from ..serializers.taskSerializer import TaskModelSerializer

class TaskModelList(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer

class TaskModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer