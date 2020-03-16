from django.db import models
from django.urls import reverse

class Post(models.Model):
    post_text = models.TextField(max_length=128)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_text[:50]

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    