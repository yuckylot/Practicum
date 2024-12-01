import numpy as np
from numpy.random import default_rng as rnd

def print2DArray(arr):
    if type(arr) == int:
        print("Нет матрицы")
        return
    for i in range(len(arr)):
        print(" ")
        for j in range(len(arr[0])):
            print(f"{arr[i][j]:.2f}", end=" ")

my_array = np.arange(10, 70, 2)
print("1:\n")
print(*my_array)
print("\n")


A = my_array.reshape((6, 5))
A = A.transpose()
print("2:")
print2DArray(A)
print("\n")

A = 2.5 * A
A[0] = A[0] - 5
print("3:")
print2DArray(A)
print("\n")

B = 10 * rnd().random((6,3))
print("4:")
print2DArray(B)
print("\n")

a = np.sum(A, axis=1)
b = np.sum(B, axis=0)
print("5:\n") 
print("Размерность a: ", np.size(a)) 
print(*a)
print("Размерность b: ", np.size(b))
print(*b)
print("\n")

muti = np.matmul(A,B)
print("6: ")
print2DArray(muti) 
print("\n")

A = np.delete(A, 2, axis=1)
B = np.append(B, 20 * rnd().random((6,3)), axis=1)
print("7: ")
print2DArray(A) 
print("\n")
print2DArray(B) 
print("\n")

detA = np.linalg.det(A)
detB = np.linalg.det(B)

print("8: ")
print("Определитель A", detA) 
print("Определитель B", detB)

invA = np.linalg.inv(A) if detA !=0 else -1
invB = np.linalg.inv(B) if detB !=0 else -1
print("Обратная матрица A:")
print2DArray(invA)
print("Обратная матрица B:") 
print2DArray(invB)
print("\n")

A = np.linalg.matrix_power(A, 6)
B = np.linalg.matrix_power(B, 14)
print("9: ")
print("Матрица A:")
print2DArray(A)
print("\n")
print("Матрица B:")
print2DArray(B)
print("\n")

print("10: \n")
M1 = np.array([[2., 0., -1., 25.],
               [-6., 28., -7.4, 0.],
               [1., -5., 13., 2.8],
               [0., 4., 3., 1.7]])
v1 = [6.7, -4., 16., 8.]
solve = np.linalg.solve(M1, v1)
print(*solve)