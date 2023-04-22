##########################################################################
# Raegan Sweeney
# CS 162
# Assignment 3 (Arrays in Python)

# ---------------------------------------------------------------------- #
# IMPORT
# numpy

import numpy as np

# ---------------------------------------------------------------------- #
# ARRAY
# make here

main_array = np.random.randint(1, 10, size=(5, 5), dtype=int)

# print whole array
print(main_array)

# print row 2 column 3
print(main_array[1, 2])

# ---------------------------------------------------------------------- #
# MATH
# calculations on array

# sum of all numbers
print(np.sum(main_array, axis=None))

# print mean of each row
print(np.mean(main_array, axis=1))

# print max value of each row
print(np.amax(main_array, axis=1))
