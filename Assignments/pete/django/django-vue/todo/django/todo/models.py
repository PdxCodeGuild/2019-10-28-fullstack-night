from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now=True)
    completed = models.DateTimeField(null=True, blank=True)
    completed_bool = models.BooleanField(default=False)

    def __str__(self):
        return f"Text: {self.text}; Created on: {self.created}; Completed on: {self.completed}; Completed bool: {self.completed_bool}"