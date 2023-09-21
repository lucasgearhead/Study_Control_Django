# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Subject do seu aplicativo (assumindo que existe)
from ..models.subject import Subject

# Definindo a classe do serializador 'SubjectSerializer' que herda de 'serializers.ModelSerializer'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        # Especificando o modelo associado ao serializador
        model = Subject
        
        # Especificando que todos os campos do modelo devem ser incluídos no serializador
        fields = '__all__'
