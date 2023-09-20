from rest_framework import serializers
from ..models.disciplineModel import DisciplineModel

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineModel  
        fields = '__all__' 
