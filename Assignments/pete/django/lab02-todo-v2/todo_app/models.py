from django.db import models

class TodoItem(models.Model):
    """
    This can be done with a single model TodoItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.
    """
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=True)
    completed_date = models.DateTimeField(null=True)
    completed_bool = models.BooleanField(default=False)

    def __str__(self):
        return f"\nText: {self.text}\nCreated Date: {self.created_date}\nCompleted Date: {self.completed_date}\nCompleted Bool: {self.completed_bool}"