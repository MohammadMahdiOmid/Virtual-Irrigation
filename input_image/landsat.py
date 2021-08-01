import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# load images
blue = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Blue.tif")
green = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Green.tif")
red = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Red.tif")
nir = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/NIR.tif")

# load all images
# landsat = io.imread_collection("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/*.tif")
# print(len(landsat))
# print(landsat[3])

# shape of images
print(blue.shape)
print(green.shape)
print(red.shape)
print(nir.shape)

# change to array
b_arr = np.array(blue).astype(float)
g_arr = np.array(green).astype(float)
r_arr = np.array(red).astype(float)
n_arr = np.array(nir).astype(float)
# print(b_arr,g_arr,r_arr,n_arr)
# print(b_arr[100][25])


# dimention
print(b_arr.ndim)

# type
print(g_arr.dtype)

# size
print(r_arr.size)

# itemsize
print(n_arr.itemsize)


# To combine colors(RGB)
# stack = np.stack([b_arr, g_arr, r_arr, n_arr], axis=2)

# To normalization data between [0..1] or [0..255]
b_arr_normal = (b_arr - np.min(b_arr)) / (np.max(b_arr) - np.min(b_arr))
g_arr_normal = (g_arr - np.min(g_arr)) / (np.max(g_arr) - np.min(g_arr))
r_arr_normal = (r_arr - np.min(r_arr)) / (np.max(r_arr) - np.min(r_arr))
# n_arr_normal = (n_arr - np.min(n_arr)) / (np.max(n_arr) - np.min(n_arr))

# To combine colors(RGB)
nor_stack = np.stack([r_arr_normal, g_arr_normal, b_arr_normal], axis=2)

# To showing landsat images
plt.figure(figsize=(20, 20))
plt.title("landsat 3 images ", fontsize=30)
plt.imshow(nor_stack)
plt.axis('off')
plt.show()
plt.savefig('landsat.png')
