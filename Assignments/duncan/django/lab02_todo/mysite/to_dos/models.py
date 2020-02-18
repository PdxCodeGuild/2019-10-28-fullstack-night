from django.db import models

class Task(models.Model):
    chore_name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    completed_date = models.DateTimeField('date completed', null = True, blank = True)
    chore_status = models.BooleanField(default = False)
    def __str__(self):
        return self.chore_name