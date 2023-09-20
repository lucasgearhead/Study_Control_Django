from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.disciplineModel import DisciplineModel
from ..serializers.disciplineSerializer import DisciplineSerializer

class DisciplineList(APIView):
    def get(self, request):
        disciplines = DisciplineModel.objects.all()
        serializer = DisciplineSerializer(disciplines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplineDetail(APIView):
    def get_object(self, pk):
        try:
            return DisciplineModel.objects.get(pk=pk)
        except DisciplineModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data)

    def put(self, request, pk):
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        discipline = self.get_object(pk)
        discipline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
