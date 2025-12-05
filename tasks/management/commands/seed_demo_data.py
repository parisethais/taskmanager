from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from tasks.models import TaskType, Tag, Task
from accounts.models import Position
from datetime import date, timedelta


Worker = get_user_model()


class Command(BaseCommand):
    help = "Seed demo data for testing"

    def handle(self, *args, **kwargs):

        # --- Task Types ---
        task_types = [
            "Bug",
            "Feature",
            "Improvement",
            "Maintenance",
        ]
        task_type_objs = []
        for name in task_types:
            obj, _ = TaskType.objects.get_or_create(name=name)
            task_type_objs.append(obj)

        # --- Tags ---
        tags = ["Backend", "Frontend", "Urgent", "Low Priority", "Refactor"]
        tag_objs = []
        for name in tags:
            obj, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(obj)

        # --- Positions ---
        positions = ["Developer", "Designer", "Manager"]
        position_objs = []
        for name in positions:
            obj, _ = Position.objects.get_or_create(name=name)
            position_objs.append(obj)

        # --- Workers ---
        workers_data = [
            ("alice", "Developer"),
            ("bob", "Designer"),
            ("charlie", "Manager"),
        ]

        worker_objs = []
        for username, position_name in workers_data:
            pos = Position.objects.get(name=position_name)
            worker, created = Worker.objects.get_or_create(
                username=username,
                defaults={"position": pos},
            )
            if created:
                worker.set_password("123456")
                worker.save()
            worker_objs.append(worker)

        # --- Tasks ---
        deadlines = [
            date.today() + timedelta(days=3),
            date.today() + timedelta(days=7),
            None,
        ]

        tasks_data = [
            ("Fix login bug", "Users cannot log in sometimes.", deadlines[0], "urgent"),
            ("Create dashboard", "A simple dashboard for managers.", deadlines[1], "high"),
            ("Refactor task model", "Clean up model structure.", deadlines[2], "medium"),
        ]

        for i, (name, desc, deadline, priority) in enumerate(tasks_data):
            task_type = task_type_objs[i % len(task_type_objs)]
            task, _ = Task.objects.get_or_create(
                name=name,
                defaults={
                    "description": desc,
                    "deadline": deadline,
                    "priority": priority,
                    "task_type": task_type,
                }
            )

            task.tags.set(tag_objs[:2])

            task.assignees.set(worker_objs[:2])

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
