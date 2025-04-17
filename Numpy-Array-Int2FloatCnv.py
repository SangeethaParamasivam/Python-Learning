'''*Numpy arrays assignment questions*
1. Given an array arr = np.array([1, 2, 3, 4, 5]), convert all values to float
2. Write a program to reverse a NumPy array.
3. Create a 4x4 array with random integers between 1 and 100. Find the maximum value in each row

1. Given an array arr = np.array([1, 2, 3, 4, 5]), convert all values to float'''

import numpy as np

def convert_float(arr):

    float_arr = [float(element) for element in arr]

    return float_arr

arr = np.array([1, 2, 3, 4, 5])

float_arr = convert_float(arr)



print(float_arr)
