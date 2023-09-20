from django.urls import path

from studyControl.views.disciplineView import DisciplineDetail, DisciplineList
from studyControl.views.studentView import StudentDetail, StudentList
from studyControl.views.taskView import TaskDetail,TaskList

urlpatterns = [
    path('students', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('disciplines/', DisciplineList.as_view(), name='discipline-list'),
    path('disciplines/<int:pk>/', DisciplineDetail.as_view(), name='discipline-detail'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
