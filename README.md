# GeoDjango API Demo

This project demonstrates the major features of **GeoDjango** with a REST API built using **Django REST Framework (DRF)**. The API includes endpoints for managing **locations** and **city boundaries** while showcasing various **geospatial queries** such as proximity searches, bounding box filtering, and location filtering based on distance.

## Project Setup

To get started with this demo project, follow these steps:

### Prerequisites

- Python 3.8 or later
- Django 3.x or later
- Django REST Framework
- GeoDjango (PostGIS support)
- PostgreSQL with PostGIS extension

### Installation

1. **Clone the repository** and navigate into the project directory.
2. **Create a virtual environment** and activate it.
3. **Install the dependencies** by using the `requirements.txt` file.
4. **Set up PostgreSQL and PostGIS**:
   - Ensure you have PostgreSQL with the PostGIS extension installed and configured.
   - Create a database and enable PostGIS.
5. **Run migrations** to set up the database.
6. **Run the development server** to start the API.

The API will be accessible at `http://localhost:8000/`.

---

## API Endpoints

### **Location Endpoints**

1. **List all locations**  
   - **Method**: GET
   - **Endpoint**: `/locations/`
   - **Description**: Retrieves a list of all locations.

2. **Create a new location**  
   - **Method**: POST
   - **Endpoint**: `/locations/`
   - **Description**: Creates a new location. Requires `name`, `latitude`, and `longitude` fields.

3. **Retrieve a single location**  
   - **Method**: GET
   - **Endpoint**: `/locations/{id}/`
   - **Description**: Retrieves details of a specific location by its `id`.

4. **Update an existing location**  
   - **Method**: PUT
   - **Endpoint**: `/locations/{id}/`
   - **Description**: Updates an existing location by its `id`. Can update `name`, `latitude`, and `longitude`.

5. **Delete a location**  
   - **Method**: DELETE
   - **Endpoint**: `/locations/{id}/`
   - **Description**: Deletes a location by its `id`.

### **City Boundary Endpoints**

1. **List all city boundaries**  
   - **Method**: GET
   - **Endpoint**: `/city-boundaries/`
   - **Description**: Retrieves a list of all city boundaries.

2. **Create a new city boundary**  
   - **Method**: POST
   - **Endpoint**: `/city-boundaries/`
   - **Description**: Creates a new city boundary. Requires `name` and `boundary` (Polygon geometry).

3. **Retrieve a single city boundary**  
   - **Method**: GET
   - **Endpoint**: `/city-boundaries/{id}/`
   - **Description**: Retrieves a specific city boundary by its `id`.

4. **Update a city boundary**  
   - **Method**: PUT
   - **Endpoint**: `/city-boundaries/{id}/`
   - **Description**: Updates an existing city boundary by its `id`.

5. **Delete a city boundary**  
   - **Method**: DELETE
   - **Endpoint**: `/city-boundaries/{id}/`
   - **Description**: Deletes a city boundary by its `id`.

---

## Geospatial Query APIs

These API endpoints demonstrate advanced **GeoDjango** queries such as distance-based filtering, bounding box queries, and more.

### **Nearest Location API**

- **Method**: GET
- **Endpoint**: `/locations/nearest/`
- **Query Parameters**:
  - `lat`: Latitude of the user.
  - `lon`: Longitude of the user.
- **Description**: Finds the nearest location to the given latitude and longitude within a 5 km radius.

### **Location within Bounding Box API**

- **Method**: GET
- **Endpoint**: `/locations/bbox/`
- **Query Parameters**:
  - `min_lat`: Minimum latitude of the bounding box.
  - `min_lon`: Minimum longitude of the bounding box.
  - `max_lat`: Maximum latitude of the bounding box.
  - `max_lon`: Maximum longitude of the bounding box.
- **Description**: Returns all locations within the provided bounding box (defined by minimum and maximum latitudes and longitudes).

### **Locations within a Distance API**

- **Method**: GET
- **Endpoint**: `/locations/within_distance/`
- **Query Parameters**:
  - `lat`: Latitude of the user.
  - `lon`: Longitude of the user.
  - `distance`: Radius (in meters) to search within (default is 1000 meters).
- **Description**: Filters locations that are within a given distance from the provided latitude and longitude.

### **Locations in City Boundary API**

- **Method**: GET
- **Endpoint**: `/locations/in_city_boundary/`
- **Query Parameters**:
  - `city_id`: ID of the city boundary.
- **Description**: Filters locations that are within a specific city boundary defined by the `city_id`.

### **Locations Near City Center API**

- **Method**: GET
- **Endpoint**: `/locations/near_city_center/`
- **Query Parameters**:
  - `radius`: Radius (in meters) around the city center to search within (default is 5000 meters).
- **Description**: Filters locations that are within a specified radius from the center of the city (e.g., New York City center).

---

## Models

### **Location Model**

- Represents a geographic location with a name and a point (latitude and longitude).

### **CityBoundary Model**

- Represents the boundary of a city using a polygon geometry.

---

## Additional Features

### **GeoDjango's Geospatial Fields**:
- **PointField**: Represents a point in 2D space (e.g., latitude/longitude).
- **PolygonField**: Represents a polygon (e.g., a city boundary).
- **Distance**: Can be used for distance calculations.
- **Indexing**: All geospatial fields are indexed using PostGIS for optimized queries.

### **GeoDjango Query Features**:
- **distance**: Calculate the distance between geometries.
- **within**, **intersects**, **contains**: Perform spatial queries to check if geometries are within another geometry, intersect, or contain other geometries.
- **buffer()**: Create a buffer (a circular area) around a geometry.

---

## Conclusion

This demo showcases various **GeoDjango** features, including **geospatial fields**, **distance-based filtering**, and **bounding box queries**. The project can be easily extended to handle more complex geospatial use cases.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
