import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# load images
blue = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Blue.tif")
green = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Green.tif")
red = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/Red.tif")
nir = io.imread("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/NIR.tif")

#load all images
landsat=io.imread_collection("E:/Company/KAVOSHGARAN/Virtual Irrigation/Image/Landsat/*.tif")
print(len(landsat))
print(landsat[3])

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

