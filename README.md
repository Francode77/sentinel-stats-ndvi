# Project Sentinel statistical API

In this notebook I explore the use of Sentinel statistical API to gather NDVI data in a 3 year timespan for two agricultural fields in Flanders region.

# Usage
Download the source .TIFF file from [this link](https://www.mediafire.com/view/p5mz28kul0gwldg/response.tiff/file)

- Copy this file to `data/sentinel2/source`

Download the source geodata for agricultural areas in Flanders from [this link](https://www.mediafire.com/file/my7zyicbov9p1hl/Shapefile.7z/file)

- Extract this file into `data/agriculture_geodata`

Create a virtual environment with Python 3.10

Install the necessary libraries with

`pip install -r requirements.txt`

# Method

1. Obtaining the labels
2. Conversion to UTM31
3. Selecting a field
4. Obtaining statistical data from Sentinel2
5. Cleaning the data
6. Result

# Further info

Scripts, classes and functions are located in the `scripts` folder

Outputs from UTM conversion are saved in the `data/processed` folder

Outputs from the violin-charts are saved in the `data/export` folder

# Contributors

This notebook was written by Frank Trioen, April 2023.
