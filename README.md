# Portland Grocery Accessibility
This project aims to assess and visualize grocery store accessibility in Portland, Oregon, by providing a scoring system for address-based grocery proximity and creating interactive heatmaps to highlight underserved areas. The goal is to shed light on gaps in grocery accessibility and help inform community-focused investments.

## Structure
```
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
```

## Requirements
Install dependencies using:
`pip install -r requirements.txt`

## Environment Variables
Set the following environment variables for ArcGIS API access:
- `ARCGIS_ACCESS_TOKEN`: Your ArcGIS access token
- `ARCGIS_USERNAME`: Your ArcGIS username
- `ARCGIS_PASSWORD`: Your ArcGIS password

