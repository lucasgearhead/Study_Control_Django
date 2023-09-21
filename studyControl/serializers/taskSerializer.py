# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Task do seu aplicativo (assumindo que existe)
from ..models.task import Task

# Definindo a classe do serializador 'TaskSerializer' que herda de 'serializers.ModelSerializer'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Especificando o modelo associado ao serializador
        model = Task
        
        # Especificando que todos os campos do modelo devem ser incluídos no serializador
        fields = '__all__'
