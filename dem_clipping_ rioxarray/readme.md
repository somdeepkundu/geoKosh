# Purulia SRTM Mosaicing and Clipping


**A Python/Colab pipeline to download, mosaic, and clip SRTM DEM data for Purulia District, India**

![bbox](https://github.com/user-attachments/assets/4a95fbc6-732d-4829-abf0-d68c73b8c176)

---

## Overview

This repository contains a complete, reproducible workflow for processing Shuttle Radar Topography Mission (SRTM) data for the Purulia region in West Bengal, India.  
The pipeline downloads SRTM tiles, mosaics them, and clips the result to the district boundary using open-source geospatial Python tools (rasterio, geopandas, etc.), and is designed to run easily on this [Google Colab notebook](https://colab.research.google.com/drive/18UuRIa1y9twIXAmNs9lV-gaOVPe0AJ5w?usp=sharing/).

---

## Features

- Automated download of SRTM .hgt.zip files from GitHub/raw URLs
- Download and use of district boundary shapefile
- Raster mosaicing and seamless merging of tiles
- Clipping to the Purulia administrative boundary
- Output in standard GeoTIFF format
- All steps fully reproducible in a single Jupyter notebook


---

## Requirements

- Python 3.x (Google Colab or local)
- Key libraries: geopandas, rasterio, numpy, matplotlib, requests

All dependencies are installed in the notebook cells.

---

## How to Run

1. **Open the notebook in Google Colab**:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_NOTEBOOK_LINK_HERE)

2. **Run each cell sequentially**:  
   The notebook will automatically download data, process, and save outputs in `/content/output`.

3. **Modify for your own region**:  
   Replace the SRTM tile URLs and boundary shapefile with those for your area of interest.

---

## Data Sources

- **SRTM 1 Arc-Second DEM** NASA Shuttle Radar Topography Mission Global 1 arc second provided by The Land Processes Distributed Active Archive Center (LP DAAC). Downloaded using the [30-Meter SRTM Tile Downloader](https://dwtkns.com/srtm30m/).
- **District boundary shapefile - Survay of India**:  
  [SOI Onlinemaps portal](https://onlinemaps.surveyofindia.gov.in/Home.aspx)

---

Feel free to open issues or contribute improvements!



