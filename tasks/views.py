from django.shortcuts import render
from .models import Task

def task_list(request):
    completed_tasks = Task.objects.filter(is_completed=True)
    incomplete_tasks = Task.objects.filter(is_completed=False)

    return render(request, 'tasks/task_list.html',
                  {'completed_tasks': completed_tasks,
                   'incomplete_tasks': incomplete_tasks}
                  )
