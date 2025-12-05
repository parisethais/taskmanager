from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    completed_tasks = Task.objects.filter(is_completed=True)
    incomplete_tasks = Task.objects.filter(is_completed=False)

    context = {
        "completed_tasks": completed_tasks,
        "incomplete_tasks": incomplete_tasks,
    }
    return render(request, "tasks/task_list.html", context)


@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")
    else:
        return render(request, "tasks/task_confirm_delete.html", {"task": task})
