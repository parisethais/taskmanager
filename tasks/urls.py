from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete

app_name = "tasks"

urlpatterns = [
    path("", task_list, name="task_list"),
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("task/create/", task_create, name="task_create"),
    path("<int:pk>/update/", task_update, name="task_update"),
    path("<int:pk>/delete/", task_delete, name="task_delete"),
]
