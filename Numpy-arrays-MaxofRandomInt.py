'''*Numpy arrays assignment questions*
1. Given an array arr = np.array([1, 2, 3, 4, 5]), convert all values to float
2. Write a program to reverse a NumPy array.
3. Create a 4x4 array with random integers between 1 and 100. Find the maximum value in each row

3. Create a 4x4 array with random integers between 1 and 100. Find the maximum value in each row'''

import numpy as np



random_num = np.random.randint(1, 101, size=(4, 4))

arr_max = np.max(random_num, axis=1)


print("4D array:")

print(random_num)

print("Maxima of array:")

print(arr_max)
