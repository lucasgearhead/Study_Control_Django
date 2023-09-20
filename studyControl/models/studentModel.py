from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name