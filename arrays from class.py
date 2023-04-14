# Array without Numpy
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#print the item in row 2 column 2
print(matrix)
print(matrix[2][2])

for row in matrix:
    for item in row:
        pass
        print(item)
        
import numpy as np

arrayn = np.array([[1,2,3],[4,5,6] ,[8,9,10]])
print(arrayn)
print (arrayn.shape)

for row in arrayn:
    for item in row:
        print(item)
#print the item in row 1 column 1
print(arrayn[1][1])

#sum and then print the sum of axis 1, column 2
summer = np.sum([[1,2,3],[4,5,6] ,[8,9,10]],axis = 0)
print(summer[2])

