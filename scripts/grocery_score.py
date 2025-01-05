# Script to calculate grocery accessibility score

# Geocode the Portland address into latitude and longitude
from arcgis.geocoding import geocode
from arcgis.gis import GIS
from dotenv import load_dotenv
import requests
import os
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points

# Load environment variables from the .env file
load_dotenv()

# ArcGIS Places API Configuration
BASE_URL = "https://places-api.arcgis.com/arcgis/rest/services/places-service/v1"
ACCESS_TOKEN = os.getenv("ARCGIS_ACCESS_TOKEN")  # Load access token from the .env file
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Helper function to call ArcGIS Places API
def find_nearby_groceries(lat, lon, radius=5000):
    url = f"{BASE_URL}/places/near-point"
    params = {
        "location": f"{lat},{lon}",
        "categories": "100-02-00",  # Example category ID for grocery stores
        "radius": radius,
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_coordinates(address):
    gis = GIS("https://www.arcgis.com", os.getenv("ARCGIS_USERNAME"), os.getenv("ARCGIS_PASSWORD"))
    result = geocode(address)
    if result:
        location = result[0]['location']
        return location['x'], location['y']
    return None, None

# Calculate the distance from the input address to the nearest grocery store
def calculate_distance_score(address_coords, grocery_data):
    if address_coords == (None, None):
        return "Invalid Address"
    user_point = Point(address_coords)
    grocery_points = gpd.points_from_xy(
        [place["geometry"]["x"] for place in grocery_data["features"]],
        [place["geometry"]["y"] for place in grocery_data["features"]]
    )
    grocery_geoseries = gpd.GeoSeries(grocery_points)
    nearest_geom = nearest_points(user_point, grocery_geoseries.unary_union)[1]
    min_distance = user_point.distance(nearest_geom)

    # Convert distance to a 1-10 score (example scaling)
    return max(1, 10 - int(min_distance / 1000))

# Combine Address Input and Distance Score:
def grocery_accessibility_score(address):
    coords = get_coordinates(address)
    if coords == (None, None):
        return "Invalid Address"

    # Use ArcGIS Places API to fetch nearby grocery data
    grocery_data = find_nearby_groceries(coords[0], coords[1])
    if not grocery_data:
        return "Error fetching grocery data"

    return calculate_distance_score(coords, grocery_data)

if __name__ == "__main__":
    test_address = "Your Test Address Here"
    score = grocery_accessibility_score(test_address)
    print(f"Grocery Accessibility Score: {score}")
