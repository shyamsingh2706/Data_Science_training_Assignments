
import numpy as np
import matplotlib.pyplot as plt

matrix_1_lst = [ [1,2],
                 [3,4]  ]

#pull rank of a matrix
rnk = np.linalg.matrix_rank(matrix_1_lst)

print ("matrix rank is {}.".format(rnk))

if rnk == len(matrix_1_lst):

    print("Inverse matrix is possible as its a FULL rank matrix " )
    matrix_1_array = np.array(matrix_1_lst)
    matrix_1_inverse = np.linalg.inv(matrix_1_array)
    print ( "Inverse matrix is {}".format(matrix_1_inverse))

    ''' checking if Inverse and Original matrix is giving  Identity Matrix '''
    matrix_UT_Check = np.dot(matrix_1_array,matrix_1_inverse)
    print("Multiplication of Matrix and Inverse matrix is {}".format(matrix_UT_Check))
else:
    print("Its a singular matrix , Inverse is not possible ")


print("checking Determinant of the Matrix")

mat_determinant = np.linalg.det(matrix_1_lst)
print("Determinant of Matrix is {}".format(mat_determinant))

