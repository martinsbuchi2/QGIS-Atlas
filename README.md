# QGIS-Atlas
================

### Overview

QGIS Atlas is a powerful tool for automating the creation of map series by generating multiple maps based on data from a single layout template. Combined with QGIS expressions, it enables dynamic customization of map elements, such as labels, symbology, and annotations, tailored to each feature in the dataset. This automation streamlines repetitive mapping tasks, ensures consistency, and enhances efficiency in producing professional-quality maps, making it ideal for large-scale projects like site selection, land-use planning, and reporting.

### Step-by-step approach to this automation

-Prepare Your Data
    -Load your spatial dataset (e.g., shapefiles, GeoJSON, or database layers) into QGIS.
    -Ensure the attribute table contains fields for labeling, filtering, or any customizations needed for the map series.

-Design the Map Layout
    -Open the Print Layout in QGIS and create a new layout.
    -Add map elements like the main map frame, legends, scale bars, north arrows, and labels.

-Enable QGIS Atlas
    -In the Print Layout, go to the Atlas panel and check Generate an Atlas.
    -Select the layer containing the features you want to iterate over as the Coverage Layer.

-Configure Coverage Settings
    -Set the feature filtering options, such as defining subsets using expressions or selecting a field for feature order.
    -Enable the Controlled Map Extent option to ensure the map adjusts its view to the current feature.

-Customize Map Elements with Expressions
    -Use QGIS Expressions to dynamically adjust text or visual elements based on the attributes of the coverage layer.
    -For example:
        -Labels: Use expressions like "Region_Name" for dynamic text.
        -Titles: Add a dynamic title using concat('Map of ', "Region_Name").
        -Symbology: Apply categorized or rule-based symbology tied to attribute fields.

-Test the Atlas
    -Use the Preview Atlas option in the Atlas panel to review each map iteration.
    -Check for errors or inconsistencies in map extent, labels, or symbology.

-Export the Map Series
    -In the Atlas panel, choose the export format (e.g., PDF, PNG).
    -Specify file naming conventions, often using expressions like "Region_Name" || '.pdf' for unique file names.

-Refine and Finalize
    -Review the exported maps for consistency and accuracy.
    -Adjust layout or symbology as needed and re-export if necessary.

-Automate Further (Optional)
    -Use QGIS’s Python API (PyQGIS) to script the entire process for large-scale or repeatable tasks.


# PDF Compression Script

This repository contains Python scripts for compressing and optimizing PDF files. The scripts reduce file sizes by removing unnecessary data, optimizing images, and adjusting resolution, making it ideal for sharing or archiving large PDF files.

## Features
- Compress individual or multiple PDF files.
- Supports optimization using **PyPDF2**, **PikePDF**, or **Ghostscript**.
- Batch processing for folders of PDFs.
- Adjustable image resolution for better size-quality balance.

## Requirements
Ensure you have Python installed, along with the following libraries:
- `PyPDF2`: Lightweight compression and PDF manipulation.
- `pikepdf`: Advanced PDF optimization with image handling.
- **Optional:** Ghostscript for high-level compression and fine control.

Install the required libraries using:
```bash
pip install PyPDF2 pikepdf
