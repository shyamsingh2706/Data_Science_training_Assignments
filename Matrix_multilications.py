import numpy as np

matrix_1= [[1,2,3,4],
           [5,6,7,8],
           [9,1,2,3],
           [4,5,6,7]]

matrix_2= [[1,5,9],
           [2,6,1],
           [3,7,2],
           [4,8,3]]

Dot_matrix_loop = [[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]


#Matrix calculation using Loops ( Dot product )
for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_2)):
            # resulted matrix
            Dot_matrix_loop[i][j] += matrix_1[i][k] * matrix_2[k][j]

#print(np.array(Dot_matrix_loop))

# Dot product using numpy

Dot_matrix_numpy = np.dot(matrix_1, matrix_2)
#print(Dot_matrix_numpy)

mtx_1_arr = np.array(matrix_1)
mtx_2_arr = np.array(matrix_2)

#Dot product using numpy array loop

Dot_matrix_loop_numpy = [[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]


for i in range(len(mtx_1_arr)) :
    matrix_temp_1=mtx_1_arr[i:i+1,:]
    for j in range(len(mtx_2_arr[0])) :
         matrix_temp_2 = mtx_2_arr[:,j:j+1]
         # print(matrix_temp_1)
         # print(matrix_temp_2)
         num = (np.dot(matrix_temp_1,matrix_temp_2))
         Dot_matrix_loop_numpy[i][j]= num.item()

#print(np.array(Dot_matrix_loop_numpy))

##Row Method using numpy array loop

Row_Method_matrix = [[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]

temp_list=[]

for j in range(len(mtx_1_arr[0])):
    for k in range(len(mtx_2_arr)):
        temp_list = (mtx_1_arr[j][k] * mtx_2_arr[k])
        Row_Method_matrix[j] += temp_list

#print(np.array(Row_Method_matrix))

##Column product using numpy array loop

Column_Method_matrix = [[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]

col_matrix_arr = np.array(Column_Method_matrix)

temp_list=[]
temp_list_2=[ [0],[0],[0],[0]]

for i in range(len(mtx_2_arr)-1):
        temp_list = []
        temp_list_2 = [[0], [0], [0], [0]]
        for k in range(len(mtx_1_arr[0])):
            temp_list =  (mtx_2_arr[ k:k+1,i:i+1]) * (mtx_1_arr[:,k:k+1])
            temp_list_2 += temp_list
        col_matrix_arr[:,i:i+1] = temp_list_2

#print(np.array(col_matrix_arr))



#Outer product using numpy array loop

outer_product_numpy = [[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]

for j in range(len(mtx_2_arr)) :
         matrix_temp_1 = mtx_1_arr[ :, j:j+1]
         matrix_temp_2 = mtx_2_arr[j:j+1,:]
         # print (matrix_temp_1)
         # print(matrix_temp_2)
         num = np.dot(matrix_temp_1,matrix_temp_2)
         # print(num)
         outer_product_numpy += num

#print(np.array(outer_product_numpy))



