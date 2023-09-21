# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Student do seu aplicativo (assumindo que existe)
from ..models.student import Student

# Definindo a classe do serializador 'StudentSerializer' que herda de 'serializers.ModelSerializer'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        # Especificando o modelo associado ao serializador
        model = Student
        
        # Especificando que todos os campos do modelo devem ser incluídos no serializador
        fields = '__all__'
