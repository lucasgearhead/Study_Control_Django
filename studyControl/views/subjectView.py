# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo Subject e o serializador SubjectSerializer do seu aplicativo (assumindo que existem)
from ..models.subject import Subject
from ..serializers.subjectSerializer import SubjectSerializer

# Definindo a classe de visualização 'SubjectListCreateView' que herda de 'APIView'
class SubjectListCreateView(APIView):
    def get(self, request):
        # Obtém todas as disciplinas do banco de dados
        subjects = Subject.objects.all()
        
        # Serializa a lista de disciplinas
        serializer = SubjectSerializer(subjects, many=True)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def post(self, request):
        # Serializa os dados recebidos na requisição
        serializer = SubjectSerializer(data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva o objeto Subject no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Definindo a classe de visualização 'SubjectDetailView' que herda de 'APIView'
class SubjectDetailView(APIView):
    def get_object(self, pk):
        try:
            # Tenta obter um objeto Subject com base no 'pk' fornecido
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            # Se o Subject não existe, levanta uma exceção Http404
            raise Http404

    def get(self, request, pk):
        # Obtém o objeto Subject com base no 'pk'
        subject = self.get_object(pk)
        
        # Serializa o objeto Subject
        serializer = SubjectSerializer(subject)
        
        # Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.data)

    def put(self, request, pk):
        # Obtém o objeto Subject com base no 'pk'
        subject = self.get_object(pk)
        
        # Serializa os dados recebidos na requisição e associa-os ao objeto Subject
        serializer = SubjectSerializer(subject, data=request.data)
        
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva as alterações no objeto Subject no banco de dados
            serializer.save()
            
            # Retorna os dados serializados em uma resposta HTTP
            return Response(serializer.data)
        
        # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Obtém o objeto Subject com base no 'pk'
        subject = self.get_object(pk)
        
        # Exclui o objeto Subject do banco de dados
        subject.delete()
        
        # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído com sucesso
        return Response(status=status.HTTP_204_NO_CONTENT)
