from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    delivery_date = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return self.title  

    def is_completed(self):
        return self.completed