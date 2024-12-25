Portland Grocery Accessibility Project
This project aims to assess and visualize grocery store accessibility in Portland, Oregon, by providing a scoring system for address-based grocery proximity and creating interactive heatmaps to highlight underserved areas. The goal is to shed light on gaps in grocery accessibility and help inform community-focused investments.

Project Overview
Objective
Provide an address-based score (1-10) to measure grocery accessibility in Portland.
Create a heatmap of grocery store locations to identify underserved areas.
Leverage ArcGIS Hub APIs for interactive mapping and data analysis.
Features
Grocery Accessibility Scoring: Accepts an address in Portland and returns a proximity score based on the distance to the nearest grocery stores.
Interactive Heatmap: Visualizes grocery store density across Portland neighborhoods.
Data-Driven Insights: Uses geospatial analysis to identify areas with limited grocery access.

## Structure
portland-grocery/
├── data/
│   ├── grocery_stores.csv       # Data containing grocery store locations
│   ├── demographics.geojson     # Optional: Portland neighborhood demographic data
│   └── output/                  # Folder for generated heatmaps and results
├── scripts/
│   ├── grocery_score.py         # Script for calculating grocery accessibility scores
│   ├── arcgis_hub_map.py        # Script for creating and interacting with ArcGIS Hub maps
├── venv/                        # Virtual environment folder
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation


## Requirements
Install dependencies using:
`pip install -r requirements.txt`

