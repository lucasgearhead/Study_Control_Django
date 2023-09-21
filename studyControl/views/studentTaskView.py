from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.studentModel import StudentModel
from ..models.taskModel import TaskModel
from ..serializers.taskSerializer import TaskSerializer

class StudentTaskView(APIView):
    def get(self, request, aluno_id):
        try:
            aluno = StudentModel.objects.get(pk=aluno_id)
        except StudentModel.DoesNotExist:
            return Response({"error": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        tarefas = TaskModel.objects.filter(aluno=aluno)
        serializer = TaskSerializer(tarefas, many=True)
        return Response(serializer.data)