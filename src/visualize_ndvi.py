"""
Visualizes NDVI for both years side-by-side, and also plots a
true-color image for reference so you can compare "what it looks like"
vs "what NDVI shows."
"""

import rasterio
import numpy as np
import matplotlib.pyplot as plt

def load_ndvi(path):
    with rasterio.open(path) as src:
        return src.read(1)

def load_true_color(path):
    with rasterio.open(path) as src:
        # B4=Red(4), B3=Green(3), B2=Blue(2) -> stack for RGB display
        red = src.read(4).astype('float32')
        green = src.read(3).astype('float32')
        blue = src.read(2).astype('float32')
        rgb = np.dstack((red, green, blue))
        # Normalize to 0-1 range for display (scale by typical Sentinel-2 reflectance max)
        rgb = np.clip(rgb / 3000, 0, 1)
        return rgb

# Load data
ndvi_2017 = load_ndvi("data/processed/mumbai_2017_ndvi.tif")
ndvi_2023 = load_ndvi("data/processed/mumbai_2023_ndvi.tif")
rgb_2017 = load_true_color("data/processed/mumbai_2017_merged.tif")
rgb_2023 = load_true_color("data/processed/mumbai_2023_merged.tif")

# Plot: 2 rows (true color, NDVI) x 2 columns (2017, 2023)
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

axes[0, 0].imshow(rgb_2017)
axes[0, 0].set_title("2017 - True Color")
axes[0, 0].axis('off')

axes[0, 1].imshow(rgb_2023)
axes[0, 1].set_title("2023 - True Color")
axes[0, 1].axis('off')

ndvi_plot1 = axes[1, 0].imshow(ndvi_2017, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[1, 0].set_title("2017 - NDVI")
axes[1, 0].axis('off')
fig.colorbar(ndvi_plot1, ax=axes[1, 0], fraction=0.046, pad=0.04)

ndvi_plot2 = axes[1, 1].imshow(ndvi_2023, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[1, 1].set_title("2023 - NDVI")
axes[1, 1].axis('off')
fig.colorbar(ndvi_plot2, ax=axes[1, 1], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.savefig("outputs/ndvi_comparison.png", dpi=150)
print("Saved plot to outputs/ndvi_comparison.png")
plt.show()
