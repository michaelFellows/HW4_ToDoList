from django.db import models


class Todo(models.Model):
    task_name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
