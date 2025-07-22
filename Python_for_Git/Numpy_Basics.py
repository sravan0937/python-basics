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
array1=np.arange(0,12)
matrix1=array1.reshape(3,4)
print(f"Reshaped Array:\n{matrix1}")
print(f"sum of all elements: {matrix1.sum()}")
print(f"sum of each column: {matrix1.sum(axis=0)}")
print(f"sum of each row: {matrix1.sum(axis=1)}")
print(f"greater than 5: {array1[array1 > 5]}")
print(F"array1 with multiple 3: {matrix1 * 3}")
reshaped_array = matrix1.reshape(2, -1)
print(f"Reshaped array with -1:\n{reshaped_array}")
arr = np.array([[25, 30, 35],
                [10, 50, 60],
                [21, 22, 23],
                [40, 18, 44]])
mask=np.any(arr<20, axis=1)
print(f"Mask for rows with any element < 20:\n{mask}")
mask2=np.all(arr>25,axis=0)
print(f"Mask for columns with all elements > 25:\n{mask2}")
evenmask=np.all(arr % 2 == 0, axis=1)
print(f"number of rows with all elements even:\n{len(evenmask)}")
morethan100=np.all(arr > 100, axis=1)
print(f"Rows with all elements greater than 100:\n{morethan100}")
m1 = np.array([[10, 20], [30, 40]])
m2 = np.array([[10, 60], [30, 40]])
if np.all(m1 < 50):
    print(f"diagonal elements of m1 are less than 50:\n{np.diagonal(m1)}") 
if np.all(m2 < 50):
    print(f"diagonal elements of m2 are less than 50:\n{np.diagonal(m2)}")
#confusion program
import numpy as np

# Actual and predicted results
actual = np.array([1, 0, 1, 1, 0])
pred   = np.array([1, 1, 1, 0, 0])

# Count each case using masks
TP = np.sum((actual == 1) & (pred == 1))  # True Positive
TN = np.sum((actual == 0) & (pred == 0))  # True Negative
FP = np.sum((actual == 0) & (pred == 1))  # False Positive
FN = np.sum((actual == 1) & (pred == 0))  # False Negative

# Build confusion matrix
conf_matrix = np.array([[TN, FP],
                        [FN, TP]])

print("Confusion Matrix:")
print(conf_matrix)

