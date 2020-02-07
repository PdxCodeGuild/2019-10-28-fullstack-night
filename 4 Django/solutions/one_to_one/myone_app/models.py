from django.db import models

class Key(models.Model):
    string = models.CharField(max_length=32)
    def __str__(self):
        return self.string
    

class Value(models.Model):
    from_key = models.OneToOneField(Key, on_delete = models.CASCADE, primary_key=True)
    string = models.CharField(max_length=32)
    def __str__(self):
        return self.string
