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
from shapely.ops import nearest_points

def calculate_distance_score(address_coords, grocery_data):
    if address_coords == (None, None):
        return "Invalid Address"
    user_point = Point(address_coords)
    grocery_points = gpd.points_from_xy(grocery_data['longitude'], grocery_data['latitude'])
    grocery_geoseries = gpd.GeoSeries(grocery_points)
    nearest_geom = nearest_points(user_point, grocery_geoseries.unary_union)[1]
    min_distance = user_point.distance(nearest_geom)

    # Convert distance to a 1-10 score (example scaling)
    return max(1, 10 - int(min_distance / 1000))


# Combine Address Input and Distance Score:
def grocery_accessibility_score(address, grocery_data):
    coords = get_coordinates(address)
    return calculate_distance_score(coords, grocery_data)
