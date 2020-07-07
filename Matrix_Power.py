
''' find Eigen Vector and Eigen Value for Matrix matrix_1_lst
and then further derive matrix_1_lst using Eigen decompoition and Matrix Diagonalization'''

import numpy as np

matrix_1_lst = [ [2,0,1],
                 [1,1,2],
                 [-1,0,-2]
                ]

eign_details = np.linalg.eig(matrix_1_lst)
print ( "Eigen value for this matrix is  {}".format(eign_details[0]))
print ( "Eigen vector for this matrix P is  {}".format(eign_details[1]))

eigen_vector_inverse = np.linalg.inv(eign_details[1])
eigen_value_diagonal = np.diag(eign_details[0])
Diagonal_matrix_power_of_50 = np.linalg.matrix_power(eigen_value_diagonal,50)

print ( "Eigen vector for Inverse matrix P^-1 is  {}".format(eigen_vector_inverse))
print ( "Eigen Value's Diagonal matrix D is  {}".format(eigen_value_diagonal))
print ( "Diagonal matrix D power of 50 is  {}".format(Diagonal_matrix_power_of_50))

final_matrix_A = np.dot(eign_details[1],np.dot(eigen_value_diagonal,eigen_vector_inverse))
print ( "final Matrix A  after Eigen decompostion and diagonalization is {}" .format(final_matrix_A))

final_matrix_B = np.dot(eign_details[1],np.dot(Diagonal_matrix_power_of_50,eigen_vector_inverse))
print ( "final Matrix B  ( A^50)  is {}" .format(final_matrix_B))