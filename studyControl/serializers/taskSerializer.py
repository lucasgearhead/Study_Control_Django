from rest_framework import serializers

from ..models.taskModel import TaskModel
from ..models.studentModel import StudentModel

from .disciplineSerializer import DisciplineSerializer

class TaskSerializer(serializers.ModelSerializer):

    disciplines = DisciplineSerializer(many=True)  # Serializer para o relacionamento Many-to-Many
    student = serializers.PrimaryKeyRelatedField(queryset=StudentModel.objects.all())  # Chave estrangeira para Aluno

    class Meta:
        model = TaskModel  
        fields = ('id', 'title', 'description', 'delivery_date', 'completed', 'student', 'disciplines')
        
