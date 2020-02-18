from django.db import models

class Task(models.Model):
    chore_name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField('date completed', null = True)
    chore_status = models.BooleanField()
    

