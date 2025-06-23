"""
NumPy Stands for Numerical Python
NumPy is a powerful Python library used for numerical computing. 
It provides support for large, multi-dimensional arrays and matrices
,along with a collection of mathematical functions to operate on these arrays efficiently.
"""

import numpy as np
array_from_list = np.array([1,2,3,4,5])
print(array_from_list)
print(type(array_from_list))

#2d array
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)
print(type(array_2d))

#3d array
array_3d =  np.array([[[1,2],
                       [3,4]],
                      [[5,6],
                       [7,8]]])
print(array_3d)
print(array_3d.ndim) # ndim gives the number of dimensions of the array (output 3)
print(array_3d.shape) # Prints the shape (dimensions) of the array as a tuple (number of blocks, rows, columns)
print(array_3d.dtype) # Prints the type of a array
print(array_3d.itemsize) # Itemsizes returns the size in bytes of each element in the array
print(array_3d.data) # data, provide a direct buffer to the memory location where the array data is actually stored

print(array_from_list[3])
print(array_2d[2][2])
print(array_3d[0][1][0])

# Slicing
print(array_from_list[1:4])
print(array_2d[1:2,1:])
print(array_3d[0:2,1,1:])
