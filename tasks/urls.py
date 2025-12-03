from django.urls import path
from .views import task_list, task_detail

app_name = 'tasks'

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
]
