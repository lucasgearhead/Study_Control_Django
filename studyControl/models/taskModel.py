from django.db import models
from .disciplineModel import DisciplineModel
from .studentModel import StudentModel

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    delivery_date = models.DateField()
    completed = models.BooleanField()
    
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    disciplines = models.ManyToManyField(DisciplineModel)

    def __str__(self):
        return f"Task [{self.title} - {self.description} - {self.delivery_date} - {self.completed}]"
