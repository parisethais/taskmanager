from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import Worker
from tasks.models import Task

@login_required
def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'accounts/worker_list.html', {'workers': workers})

@login_required
def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    incomplete_tasks = Task.objects.filter(assignees=worker, is_completed=False)
    completed_tasks = Task.objects.filter(assignees=worker, is_completed=True)

    return render(
        request,
        "accounts/worker_detail.html",
        {
            "worker": worker,
            "incomplete_tasks": incomplete_tasks,
            "completed_tasks": completed_tasks,
        },
    )
