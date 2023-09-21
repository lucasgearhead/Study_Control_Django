# Importando classes necessárias do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos de Student e Task do seu aplicativo (assumindo que existem)
from ..models.student import Student
from ..models.task import Task

# Importando o serializador TaskSerializer do seu aplicativo (assumindo que existe)
from ..serializers.taskSerializer import TaskSerializer

# Definindo a classe da visualização 'StudentTasksView' que herda de 'APIView'
class StudentTasksView(APIView):
    def get(self, request, aluno_id):
        try:
            # Tenta obter um objeto Student com base no 'aluno_id' fornecido
            student = Student.objects.get(pk=aluno_id)
        except Student.DoesNotExist:
            # Se o Student não existe, retorna uma resposta 404 (Not Found)
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Filtra as tarefas relacionadas ao estudante
        tasks = Task.objects.filter(student=student)
        
        # Serializa as tarefas usando o serializador TaskSerializer com many=True
        serializer = TaskSerializer(tasks, many=True)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)
