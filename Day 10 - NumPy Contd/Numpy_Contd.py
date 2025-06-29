# Arithmetic Operations
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10, 20, 30], [40, 50, 60]])
# Add the arrays
c = a + b
# Subtract the arrays
d = a - b
# Multiply the arrays
e = a * b
# Divide the arrays
f = a / b
print("Array a:\n", a)
print("Array b:\n", b)
print("Addition:\n", c)
print("Subtraction:\n", d)
print("Multiplication:\n", e)
print("Division:\n", f)
# Comparison Operations
g = a > b
h = a < b
print("Comparison (a > b):\n", g)
print("Comparison (a < b):\n", h)   


# Methods in NumPy
# Transpose - Transposing an array swaps its rows and columns
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)
print("Transposed Array:\n", arr.T)

# Sorting - Sorting an array arranges its elements in a specified order
# Syntax: np.sort(arr, axis=-1, kind='quicksort', order=None)
arr_1D = np.array([2, 1, 3, 5, 4])
print("Original Array:\n", arr_1D)
print("Sorted Array:\n", np.sort(arr_1D))

arr_2D = np.array([[3, 1, 2], [6, 4, 5]])
print("Original 2D Array:\n", arr_2D)
print("Sorted 2D Array:\n", np.sort(arr_2D, axis=0))  # Sort along columns
print("Sorted 2D Array:\n", np.sort(arr_2D, axis=1))  # Sort along rows

arr_3D = np.array([[[3, 1], [2, 4]], [[6, 5], [8, 7]]])
print("Original 3D Array:\n", arr_3D)
print("Sorted 3D Array:\n", np.sort(arr_3D, axis=0))  # Sort along first dimension
print("Sorted 3D Array:\n", np.sort(arr_3D, axis=1))  # Sort along second dimension

# In Descending Order
print("Sorted 1D Array in Descending Order:\n", np.sort(arr_1D)[::-1])
print("Sorted 2D Array in Descending Order (axis=0):\n", np.sort(arr_2D, axis=0)[::-1])
print("Sorted 2D Array in Descending Order (axis=1):\n", np.sort(arr_2D, axis=1)[::-1])

# Argsorting - getting indices(index of orginal array position) of sorted elements
print("Indices of Sorted 1D Array:\n", np.argsort(arr_1D))
print("Indices of Sorted 2D Array (axis=0):\n", np.argsort(arr_2D, axis=0))
print("Indices of Sorted 2D Array (axis=1):\n", np.argsort(arr_2D, axis=1))
print("Indices of Sorted 3D Array (axis=0):\n", np.argsort(arr_3D, axis=0))

# Concatenation - joining two or more arrays together
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
arr_concat = np.concatenate((arr1, arr2), axis=0)  # Concatenate along rows
print("Concatenated Array along rows:\n", arr_concat)
arr_concat_col = np.concatenate((arr1, arr2), axis=1)  # Concatenate along columns
print("Concatenated Array along columns:\n", arr_concat_col)

# Reshaping - changing the shape of an array without changing its data
print("Original Array:\n", arr_1D)
reshaped_arr = arr_1D.reshape((5, 1))  # Reshape to 5 rows, 1 column
print("Reshaped Array:\n", reshaped_arr)
print("Reshaped Array to 2D:\n", arr_1D.reshape(-1)  )  # Flatten to 1D

# Splitting - dividing an array into multiple sub-arrays
print("Array to Split:\n", arr_concat)
arr_split = np.split(arr_concat, 4, axis=0)  # Split into 4 parts along rows
print("Split Array along rows:\n", arr_split)

# Statistical Functions
# Mean - average of elements
arr = np.array([[1, 2, 3], [4, 5, 6]])
mean_all = np.mean(arr)  # Mean of all elements
mean_axis0 = np.mean(arr, axis=0)  # Mean along columns
mean_axis1 = np.mean(arr, axis=1)  # Mean along rows
print("Mean of all elements:", mean_all)
print("Mean along columns:", mean_axis0)
print("Mean along rows:", mean_axis1)

# Median - middle value in sorted array
median_all = np.median(arr)  # Median of all elements
print("Median of all elements:", median_all)

# Standard Deviation - measure of spread of data
std_all = np.std(arr)  # Standard deviation of all elements
print("Standard Deviation of all elements:", std_all)

# Variance - measure of how much values differ from the mean
var_all = np.var(arr)  # Variance of all elements
print("Variance of all elements:", var_all)

# Min and Max - minimum and maximum values
min_all = np.min(arr)  # Minimum value
max_all = np.max(arr)  # Maximum value
print("Minimum value:", min_all)
print("Maximum value:", max_all)

# Sum - sum of all elements
sum_all = np.sum(arr)  # Sum of all elements
print("Sum of all elements:", sum_all)

# Miscellaneous Functions
# Zeros and Ones - creating arrays filled with zeros or ones
arr = np.zeros((2, 3))  # Create an array of zeros
print("Array of Zeros:\n", arr)
arr = np.zeros((2, 3, 4), dtype=int)  # Create a 3D array of zeros
print("3D Array of Zeros:\n", arr)

arr_1 = np.ones((2, 3))  # Create an array of ones
print("Array of Ones:\n", arr_1)
arr_2 = np.ones((2, 3, 4), dtype=int)  # Create a 3D array of ones
print("3D Array of Ones:\n", arr_2)

# Full - creating arrays filled with a specific value
arr_1d = np.full((5,), 7)  # Create a 1D array filled with 7
print("1D Array filled with 7:\n", arr_1d)

# Identity Matrix - creating an identity matrix
arr_identity = np.eye(3)  # Create a 3x3 identity matrix
print("Identity Matrix:\n", arr_identity)

# arrange - creating an array with a range of values
arr_range = np.arange(0, 10, 2)  # Create an array with values from 0 to 10 with a step of 2
print("Array with range of values:\n", arr_range)

# Random Numbers - generating random numbers
arr_random = np.random.random(5) # Create a 1D array of random numbers between 0 and 1
print("Array of Random Numbers:\n", arr_random)
arr_random_2d = np.random.random((2, 3))  # Create a 2D array of random numbers
print("2D Array of Random Numbers:\n", arr_random_2d)

np.random.seed(42)  # Set seed for reproducibility
print("Random Numbers with Seed:\n", np.random.random(5))  # Random numbers with seed

# Linespace - creating an array with evenly spaced values
# Syntax: np.linspace(start, stop, num, endpoint=True, retstep=False, dtype=None)
arr_linspace = np.linspace(0, 1, 5)  # Create an array with 5 evenly spaced values between 0 and 1
print("Array with evenly spaced values:\n", arr_linspace)

# Unique Elements - finding unique elements in an array
arr_unique = np.array([1, 2, 2, 3, 4, 4, 5])
unique_elements = np.unique(arr_unique)  # Find unique elements
print("Unique Elements:\n", unique_elements)

