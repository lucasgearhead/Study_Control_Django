# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos Student e Task e o serializador TaskSerializer do seu aplicativo (assumindo que existem)
from ..models.student import Student
from ..models.task import Task
from ..serializers.taskSerializer import TaskSerializer

# Definindo a classe de visualização 'TaskListCreateView' que herda de 'APIView'
class TaskListCreateView(APIView):
    def get(self, request):
        # Obtém todas as tarefas do banco de dados
        tasks = Task.objects.all()
        
        # Serializa a lista de tarefas
        serializer = TaskSerializer(tasks, many=True)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def post(self, request):
        # Serializa os dados recebidos na requisição
        serializer = TaskSerializer(data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva o objeto Task no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Definindo a classe de visualização 'TaskDetailView' que herda de 'APIView'
class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            # Tenta obter um objeto Task com base no 'pk' fornecido
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            # Se o Task não existe, levanta uma exceção Http404
            raise Http404

    def get(self, request, pk):
        # Obtém o objeto Task com base no 'pk'
        task = self.get_object(pk)
        
        # Serializa o objeto Task
        serializer = TaskSerializer(task)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def put(self, request, pk):
        # Obtém o objeto Task com base no 'pk'
        task = self.get_object(pk)
        
        # Serializa os dados recebidos na requisição e associa-os ao objeto Task
        serializer = TaskSerializer(task, data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva as alterações no objeto Task no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP
            return Response(serializer.data)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Obtém o objeto Task com base no 'pk'
        task = self.get_object(pk)
        
        # Exclui o objeto Task do banco de dados
        task.delete()
        
        # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído com sucesso
        return Response(status=status.HTTP_204_NO_CONTENT)
