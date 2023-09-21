# Importando a classe 'models' do módulo 'django.db'
from django.db import models

# Importando os modelos de Subject e Student do seu aplicativo (assumindo que existem)
from .subject import Subject
from .student import Student

# Definindo a classe do modelo 'Task' que herda de 'models.Model'
class Task(models.Model):
    # Definindo um campo de caractere para o título da tarefa com no máximo 100 caracteres
    title = models.CharField(max_length=100)
    
    # Definindo um campo de texto para a descrição da tarefa
    description = models.TextField()
    
    # Definindo um campo de data para a data de entrega da tarefa
    delivery_date = models.DateField()
    
    # Definindo um campo booleano para indicar se a tarefa foi concluída ou não, com valor padrão False
    completed = models.BooleanField(default=False)
    
    # Definindo um relacionamento de chave estrangeira com o modelo Student, usando 'on_delete=models.CASCADE'
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tasks')
    
    # Definindo um relacionamento muitos-para-muitos com o modelo Subject
    subjects = models.ManyToManyField(Subject, related_name='tasks')

    # Método '__str__' para retornar uma representação em string do objeto Task
    def __str__(self):
        return self.title
