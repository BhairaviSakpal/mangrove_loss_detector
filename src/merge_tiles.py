"""
Merges two-part Sentinel-2 GeoTIFF exports (from Google Earth Engine)
into a single seamless image, for each year.
"""

import rasterio
from rasterio.merge import merge
import os

def merge_tiles(part1_path, part2_path, output_path):
    """Merges two raster tiles into one and saves the result."""
    # Open both tile files
    src1 = rasterio.open(part1_path)
    src2 = rasterio.open(part2_path)

    # merge() stitches them together based on their geographic coordinates
    mosaic, out_transform = merge([src1, src2])

    # Copy metadata from one of the originals, update size/transform for the merged image
    out_meta = src1.meta.copy()
    out_meta.update({
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": out_transform
    })

    # Write the merged result to a new file
    with rasterio.open(output_path, "w", **out_meta) as dest:
        dest.write(mosaic)

    src1.close()
    src2.close()
    print(f"Saved merged file: {output_path}")


if __name__ == "__main__":
    # Merge 2023 tiles
    merge_tiles(
        "data/raw/mumbai_2023_part1.tif",
        "data/raw/mumbai_2023_part2.tif",
        "data/processed/mumbai_2023_merged.tif"
    )

    # Merge 2017 tiles
    merge_tiles(
        "data/raw/mumbai_2017_part1.tif",
        "data/raw/mumbai_2017_part2.tif",
        "data/processed/mumbai_2017_merged.tif"
    )
