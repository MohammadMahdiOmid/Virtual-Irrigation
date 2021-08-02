import gdal
import matplotlib.pyplot as plt
import numpy as np

hdf = gdal.Open('E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/MODIS/MOD09A1.A2017081.h21v05.005.2017090202638.hdf')
bands = []

for sd, des in hdf.GetSubDatasets():
    bands.append(sd)
    print(des)

# To get each band and changing to array
mod_b1 = gdal.Open(bands[0]).ReadAsArray().astype(float)
mod_b2 = gdal.Open(bands[1]).ReadAsArray().astype(float)
mod_b3 = gdal.Open(bands[2]).ReadAsArray().astype(float)
mod_b4 = gdal.Open(bands[3]).ReadAsArray().astype(float)
mod_b5 = gdal.Open(bands[4]).ReadAsArray().astype(float)
mod_b6 = gdal.Open(bands[5]).ReadAsArray().astype(float)

# normalization
norm_b1 = (mod_b1 - np.min(mod_b1)) / (np.max(mod_b1) - np.min(mod_b1))
norm_b2 = (mod_b2 - np.min(mod_b2)) / (np.max(mod_b2) - np.min(mod_b2))
norm_b3 = (mod_b3 - np.min(mod_b3)) / (np.max(mod_b3) - np.min(mod_b3))
norm_b4 = (mod_b4 - np.min(mod_b4)) / (np.max(mod_b4) - np.min(mod_b4))
norm_b5 = (mod_b5 - np.min(mod_b5)) / (np.max(mod_b5) - np.min(mod_b5))
norm_b6 = (mod_b6 - np.min(mod_b6)) / (np.max(mod_b6) - np.min(mod_b6))

# To combine colors(RGB)
layer_stack = np.stack([norm_b1, norm_b2, norm_b3], axis=2)

# Demonstrated
plt.figure(figsize=(20, 20))
plt.imshow(layer_stack)
plt.title("MODIS IMAGE", fontsize=20)
plt.axis('off')
plt.show()
