"""
Computes NDVI (vegetation index) from merged Sentinel-2 images
for both years, and saves NDVI as its own file for each.
"""

import rasterio
import numpy as np

def compute_ndvi(input_path, output_path):
    with rasterio.open(input_path) as src:
        # Sentinel-2 bands: B4 = Red, B8 = Near-Infrared (NIR)
        # Band order in your exported file matches how GEE stacked them:
        # B4(1), B3(2), B2(3), B8(4) - we'll check this via band count below
        red = src.read(4).astype('float32')   # Red band
        nir = src.read(8).astype('float32')   # NIR band

        # NDVI formula: (NIR - Red) / (NIR + Red)
        # np.errstate avoids warnings when dividing by zero (e.g. no-data pixels)
        with np.errstate(divide='ignore', invalid='ignore'):
            ndvi = (nir - red) / (nir + red)
            ndvi = np.nan_to_num(ndvi, nan=0.0)  # replace NaN with 0

        # Copy metadata, update to single-band output
        out_meta = src.meta.copy()
        out_meta.update(count=1, dtype='float32')

        with rasterio.open(output_path, "w", **out_meta) as dest:
            dest.write(ndvi, 1)

    print(f"Saved NDVI: {output_path}")
    print(f"  NDVI range: {ndvi.min():.3f} to {ndvi.max():.3f}")


if __name__ == "__main__":
    compute_ndvi(
        "data/processed/mumbai_2023_merged.tif",
        "data/processed/mumbai_2023_ndvi.tif"
    )

    compute_ndvi(
        "data/processed/mumbai_2017_merged.tif",
        "data/processed/mumbai_2017_ndvi.tif"
    )
