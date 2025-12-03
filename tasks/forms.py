from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'task_type',
            'tags',
            'assignees',
            'is_completed']
        widgets = {
            "deadline": forms.DateInput(attrs={'type': 'date'}),
            "is_completed": forms.CheckboxInput(),
        }

