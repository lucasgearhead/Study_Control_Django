# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo Student e o serializador StudentSerializer do seu aplicativo (assumindo que existem)
from ..models.student import Student
from ..serializers.studentSerializer import StudentSerializer

# Definindo a classe de visualização 'StudentListCreateView' que herda de 'APIView'
class StudentListCreateView(APIView):
    def get(self, request):
        # Obtém todos os estudantes do banco de dados
        students = Student.objects.all()
        
        # Serializa a lista de estudantes
        serializer = StudentSerializer(students, many=True)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def post(self, request):
        # Serializa os dados recebidos na requisição
        serializer = StudentSerializer(data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva o objeto Student no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Definindo a classe de visualização 'StudentDetailView' que herda de 'APIView'
class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            # Tenta obter um objeto Student com base no 'pk' fornecido
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Se o Student não existe, levanta uma exceção Http404
            raise Http404

    def get(self, request, pk):
        # Obtém o objeto Student com base no 'pk'
        student = self.get_object(pk)
        
        # Serializa o objeto Student
        serializer = StudentSerializer(student)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def put(self, request, pk):
        # Obtém o objeto Student com base no 'pk'
        student = self.get_object(pk)
        
        # Serializa os dados recebidos na requisição e associa-os ao objeto Student
        serializer = StudentSerializer(student, data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva as alterações no objeto Student no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP
            return Response(serializer.data)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Obtém o objeto Student com base no 'pk'
        student = self.get_object(pk)
        
        # Exclui o objeto Student do banco de dados
        student.delete()
        
        # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído com sucesso
        return Response(status=status.HTTP_204_NO_CONTENT)
