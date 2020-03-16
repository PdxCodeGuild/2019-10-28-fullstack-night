from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    userName = models.CharField(max_length=100)

    def __str__(self):
        return self.userName
