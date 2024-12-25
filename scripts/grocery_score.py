# Script to calculate grocery accessibility score


# Geocode the Portland address into latitude and longitude
from arcgis.geocoding import geocode
from arcgis.gis import GIS

def get_coordinates(address):
    gis = GIS()
    result = geocode(address)
    if result:
        location = result[0]['location']
        return location['x'], location['y']
    return None, None

# Calculate the distance from the input address to the nearest grocery store
import geopandas as gpd
from shapely.geometry import Point

def calculate_distance_score(address_coords, grocery_data):
    user_point = Point(address_coords)
    grocery_points = gpd.points_from_xy(grocery_data['longitude'], grocery_data['latitude'])
    grocery_geoseries = gpd.GeoSeries(grocery_points)
    distances = grocery_geoseries.distance(user_point)
    min_distance = distances.min()

    # Convert distance to a 1-10 score (example scaling)
    score = max(1, 10 - int(min_distance / 1000))
    return score


# Combine Address Input and Distance Score:
def grocery_accessibility_score(address, grocery_data):
    coords = get_coordinates(address)
    if coords:
        return calculate_distance_score(coords, grocery_data)
    else:
        return "Invalid Address"
