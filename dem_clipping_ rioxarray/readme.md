# Purulia SRTM Mosaicing and Clipping


**A Python/Colab pipeline to download, mosaic, and clip SRTM DEM data for Purulia District, India**

![aoi_bbox](https://github.com/user-attachments/assets/0def6cec-9c3a-4b05-8026-06526acfcc55)


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
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18UuRIa1y9twIXAmNs9lV-gaOVPe0AJ5w?usp=sharing)

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

---

BUILT ON THE WORKS OF UJAVAL GANDHI SIR, SPATIAL THOUGHTS

![Ff9ctKNlku0-MQ](https://github.com/user-attachments/assets/a7dc4ca9-1749-4159-bd14-7086f8e7aa4d)

[Watch YouTube Video Walkthrough](https://www.youtube.com/watch?v=Ff9ctKNlku/)
