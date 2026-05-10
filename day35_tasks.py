import numpy as np
#Matrix Traversal
matrix = [
    [1,2],
    [3,4]
]
for row in matrix:
    for element in row:
        print(element)



#Find sum of all elements
matrix = np.array([[1,2],[3,4]])
result = np.sum(matrix)
print(result)



#Matrix addition
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
sum_matrix = a+b
print(sum_matrix)



#Matrix Transpose
matrix = np.array([
    [1,2],
    [3,4]
])
transpose_of_matrix = matrix.T
print(transpose_of_matrix)



#Diagonal Sum
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

diagonal_sum = np.trace(matrix)
print(diagonal_sum)



#Largest element in matrix
matrix = np.array([
    [1,9],
    [3,4]
])
largest_element = np.max(matrix)
print(largest_element)



#Row sum
matrix = np.array([
    [1,2],
    [3,4]
])
row1 = matrix[0, ::]
row2 = matrix[1, ::]
row1_sum = np.sum(row1)
row2_sum = np.sum(row2)
print(row1_sum)
print(row2_sum)