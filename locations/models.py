# locations/models.py
from django.contrib.gis.db import models

# Model for storing a single location (Point)
class Location(models.Model):
    name = models.CharField(max_length=100)
    point = models.PointField()  # Store the location as a point (latitude, longitude)
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for storing a polygon (City boundary)
class CityBoundary(models.Model):
    name = models.CharField(max_length=100)
    boundary = models.PolygonField()  # Store city boundary as a polygon

    def __str__(self):
        return self.name
