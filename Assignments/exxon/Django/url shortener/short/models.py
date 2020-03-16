from django.db import models


class URL(models.Model):
    url_text = models.TextField()
    pub_date = models.DateTimeField("pub_date")
    short_url = models.CharField(max_length=6)

    def __str__(self):
        return self.url_text


