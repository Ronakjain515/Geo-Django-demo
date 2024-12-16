# locations/views.py
from rest_framework import generics
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.measure import D

from .models import Location, CityBoundary
from .serializers import LocationSerializer, CityBoundarySerializer

# List all locations
class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Create a new location
class LocationCreateAPIView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Retrieve a single location by its ID
class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Update an existing location by its ID
class LocationUpdateAPIView(generics.UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Delete a location by its ID
class LocationDestroyAPIView(generics.DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# List all city boundaries
class CityBoundaryListAPIView(generics.ListAPIView):
    queryset = CityBoundary.objects.all()
    serializer_class = CityBoundarySerializer

# Create a new city boundary
class CityBoundaryCreateAPIView(generics.CreateAPIView):
    queryset = CityBoundary.objects.all()
    serializer_class = CityBoundarySerializer

# Retrieve a single city boundary by its ID
class CityBoundaryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CityBoundary.objects.all()
    serializer_class = CityBoundarySerializer

# Update an existing city boundary by its ID
class CityBoundaryUpdateAPIView(generics.UpdateAPIView):
    queryset = CityBoundary.objects.all()
    serializer_class = CityBoundarySerializer

# Delete a city boundary by its ID
class CityBoundaryDestroyAPIView(generics.DestroyAPIView):
    queryset = CityBoundary.objects.all()
    serializer_class = CityBoundarySerializer


class NearestLocationAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # Get latitude and longitude from query params
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')

        if lat and lon:
            # Create a Point object from lat/lon
            user_location = Point(float(lon), float(lat), srid=4326)

            # Query for the nearest locations within a certain distance
            queryset = Location.objects.annotate(distance=user_location.distance('point')).filter(
                distance__lte=5000)  # 5 km
            queryset = queryset.order_by('distance')
            return queryset
        return Location.objects.none()


class LocationWithinBoundingBoxAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # Get the coordinates for the bounding box
        min_lat = self.request.query_params.get('min_lat')
        min_lon = self.request.query_params.get('min_lon')
        max_lat = self.request.query_params.get('max_lat')
        max_lon = self.request.query_params.get('max_lon')

        if all([min_lat, min_lon, max_lat, max_lon]):
            # Create a bounding box as a polygon
            bounding_box = Polygon.from_bbox([float(min_lon), float(min_lat), float(max_lon), float(max_lat)])

            # Filter locations within the bounding box
            return Location.objects.filter(point__within=bounding_box)
        return Location.objects.none()


class LocationsWithinDistanceAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # Get latitude, longitude and distance from query params
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        distance = self.request.query_params.get('distance', 1000)  # Default distance is 1 km

        if lat and lon:
            # Create a Point object from lat/lon
            user_location = Point(float(lon), float(lat), srid=4326)

            # Filter locations within a certain distance (in meters)
            return Location.objects.filter(point__distance_lte=(user_location, D(m=distance)))
        return Location.objects.none()


class LocationsInCityBoundaryAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # Get the city boundary ID from query params
        city_id = self.request.query_params.get('city_id')

        if city_id:
            # Get the city's boundary polygon
            city_boundary = CityBoundary.objects.get(id=city_id)
            city_polygon = city_boundary.boundary

            # Filter locations within the city boundary
            return Location.objects.filter(point__within=city_polygon)
        return Location.objects.none()


class LocationsNearCityCenterAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # City center coordinates (can be hardcoded or dynamic based on city ID)
        city_center = Point(-73.935242, 40.730610, srid=4326)  # Example: NYC center

        # Get the radius from query params (default 5000 meters or 5 km)
        radius = self.request.query_params.get('radius', 5000)

        # Filter locations within the specified radius
        return Location.objects.filter(point__distance_lte=(city_center, D(m=radius)))
