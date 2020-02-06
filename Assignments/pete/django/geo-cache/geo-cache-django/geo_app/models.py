from django.db import models

class GeoCache(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.CharField(max_length=140)

    def __str__(self):
        return f"Name: {self.name}; Latitude: {self.lat}; Longitude: {self.lng}"    