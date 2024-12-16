# locations/urls.py
from django.urls import path
from .views import (
    LocationListAPIView,
    LocationCreateAPIView,
    LocationRetrieveAPIView,
    LocationUpdateAPIView,
    LocationDestroyAPIView,
    CityBoundaryListAPIView,
    CityBoundaryCreateAPIView,
    CityBoundaryRetrieveAPIView,
    CityBoundaryUpdateAPIView,
    CityBoundaryDestroyAPIView,
    NearestLocationAPIView,
    LocationWithinBoundingBoxAPIView,
    LocationsWithinDistanceAPIView,
    LocationsInCityBoundaryAPIView,
    LocationsNearCityCenterAPIView,
)

urlpatterns = [
    # Location URLs
    path('location', LocationListAPIView.as_view(), name='location-list'),
    path('location/create', LocationCreateAPIView.as_view(), name='location-create'),
    path('location/<int:pk>/', LocationRetrieveAPIView.as_view(), name='location-retrieve'),
    path('location/update/<int:pk>/', LocationUpdateAPIView.as_view(), name='location-update'),
    path('location/delete/<int:pk>/', LocationDestroyAPIView.as_view(), name='location-delete'),

    # CityBoundary URLs
    path('city-boundaries', CityBoundaryListAPIView.as_view(), name='city-boundary-list'),
    path('city-boundaries/create', CityBoundaryCreateAPIView.as_view(), name='city-boundary-create'),
    path('city-boundaries/<int:pk>/', CityBoundaryRetrieveAPIView.as_view(), name='city-boundary-retrieve'),
    path('city-boundaries/update/<int:pk>/', CityBoundaryUpdateAPIView.as_view(), name='city-boundary-update'),
    path('city-boundaries/delete/<int:pk>/', CityBoundaryDestroyAPIView.as_view(), name='city-boundary-delete'),

    # This API will return the nearest locations to the provided coordinates within a 5 km radius.
    path('locations/nearest/<int:pk>/', NearestLocationAPIView.as_view(), name='locations-nearest'),

    # This API returns all locations that are within the defined bounding box.
    path('locations/bbox/<int:pk>/', LocationWithinBoundingBoxAPIView.as_view(), name='locations-bbox'),

    # This API will return all locations within a specified distance from the given coordinates.
    path('locations/within_distance/<int:pk>/', LocationsWithinDistanceAPIView.as_view(), name='locations-within_distance'),

    # This API will return locations that fall within the boundary of a specified city.
    path('locations/in_city_boundary/<int:pk>/', LocationsInCityBoundaryAPIView.as_view(), name='locations-in_city_boundary'),

    # This API finds locations within a specified radius from the city center.
    path('locations/near_city_center/<int:pk>/', LocationsNearCityCenterAPIView.as_view(), name='locations-near_city_center'),
]
