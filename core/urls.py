from django.urls import path
from ..studyControl.views

urlpatterns = [
    path('api/alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('api/alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
    path('api/disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('api/disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),
    path('api/tarefas/', TarefaListCreateView.as_view(), name='tarefa-list-create'),
    path('api/tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'),
]
