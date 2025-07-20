import numpy as np
#create a 3x3 array with values from 1 to 9

array=np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]) 
print(f"Original Array:\n{array}")
print(f"Shape of the array: {array.shape}")
print(f"dimensions of the array: {array.ndim}")
print(f"size of the array: {array.size}")
print(array[1])
print(array[:,-1])
array_float= array.astype(float)
print(f"Array with float type:\n{array_float}")
ones_array = np.ones((3, 2))
zeroes_array = np.zeros((3, 2))
print(f"Array of ones:\n{ones_array}")
print(f"Array of zeroes:\n{zeroes_array}")