# Mangrove Loss Detector 🌿
A machine learning project to detect and quantify mangrove forest loss in a coastal region of India using satellite imagery.

## What it does
Analyzes Sentinel-2 satellite imagery from two time periods (2017 vs. 2023) to classify mangrove cover and calculate the area lost between them, producing a visual loss heatmap and loss statistics (km² lost) for the selected region.

## Why it matters
Mangroves are critical carbon-storing coastal ecosystems, but tracking their loss manually is slow and inconsistent. This tool gives a data-backed, repeatable way to quantify loss — the kind of evidence forest departments and NGOs need to justify restoration efforts or take action against encroachment.

## Study Area
Mumbai's mangrove cover (e.g. Thane Creek / Mahim / Airoli belt), comparing 2017 vs. 2023.

## Approach
- Satellite data via Google Earth Engine (Sentinel-2 imagery)
- NDVI/NDWI-based baseline classification
- Random Forest classifier for improved mangrove/non-mangrove detection
- Pixel-wise change detection to generate loss maps and area statistics
- Interactive visualization with Folium

## Scope
This is a first ML project built by a 3-member student team, focused on Mumbai's mangrove belt comparing 2017 vs. 2023. Additional features (loss driver attribution, risk prediction, socioeconomic overlay, carbon impact estimation) are documented as future work.

## Project Structure
data/ # raw and processed satellite data (not tracked in git)
notebooks/ # Jupyter notebooks for exploration
src/ # reusable Python code (preprocessing, model, utils)
outputs/ # generated maps, charts, results
## Setup
```bash
git clone https://github.com/BhairaviSakpal/mangrove_loss_detector.git
cd mangrove_loss_detector
pip install -r requirements.txt
```

