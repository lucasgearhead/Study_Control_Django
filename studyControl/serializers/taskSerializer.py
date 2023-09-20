from rest_framework import serializers
from ..models.taskModel import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel  
        fields = '__all__' 