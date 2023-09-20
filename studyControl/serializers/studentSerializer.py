from rest_framework import serializers
from ..models.studentModel import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel  
        fields = '__all__' 