from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task

@login_required
def task_list(request):
    completed_tasks = Task.objects.filter(is_completed=True, assignees=request.user)
    incomplete_tasks = Task.objects.filter(is_completed=False, assignees=request.user)

    return render(request, 'tasks/task_list.html',
                  {'completed_tasks': completed_tasks,
                   'incomplete_tasks': incomplete_tasks}
                  )

@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

