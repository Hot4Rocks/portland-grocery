from arcgis.gis import GIS
from arcgis.mapping import WebMap
import os

def display_map():
    try:
        # Connect to ArcGIS Hub
        gis = GIS("https://www.arcgis.com", os.getenv("ARCGIS_USERNAME"), os.getenv("ARCGIS_PASSWORD"))

        # Search for your map by title
        search_results = gis.content.search("Portland Grocery Heatmap", item_type="Web Map")
        if not search_results:
            return "Map not found"
        
        webmap_item = search_results[0]

        # Load the map
        webmap = WebMap(webmap_item)

        # Open the map in a Jupyter notebook
        return webmap
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    map_view = display_map()
    if isinstance(map_view, str):
        print(map_view)
    else:
        print("Heatmap loaded successfully.")
