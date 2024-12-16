# locations/serializers.py
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Location, CityBoundary

# Serializer for the Location model
class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'point', 'description')
        geo_field = 'point'  # Specify which field is the geospatial field

# Serializer for the CityBoundary model
class CityBoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CityBoundary
        fields = ('name', 'boundary')
        geo_field = 'boundary'  # Specify the polygon field for geospatial data
