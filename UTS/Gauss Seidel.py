import numpy as np

# Mencari nilai x1, x2, dan x3 pada Sistem Persamaan Linear berikut :
# [3*x1+1*x2-1*x3 = 1]
# [2*x1+4*x2+-1*x3 = 5]
# [-1*x1+5*x2+-8*x3 = 5]

batas_iterasi = 100                                                              # Batas Iterasi
print("Menampilkan Matriks :")
A = np.array([[3., 1., -1.],
              [2., 4., -1.],
              [-1., 5., -8.],])
b = np.array([1, 5, 5])

# Mencari nilai x1, x2, dan x3 dengan menggunakan Metode Gauss Seidel
for i in range(A.shape[0]):                                                      # Misalkan nilai x1, x2, dan x3 diasumsikan ,[0 0 0]
    row = ["{0:3g} * x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
for it_count in range(1, batas_iterasi):
    x_new = np.zeros_like(x)
    print("Iterasi {0}: {1}".format(it_count, x))                                # Menampilkan x1, x2, dan x3 [0 0 0]
    for i in range(A.shape[0]):                                                  # Misalkan nilai x1, x2, dan x3 diasumsikan ,[0 0 0]
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol = 0.5):                                        # Batas Toleransi 0.5
        break
    x = x_new
    error = np.dot(A, x) - b

print("Batas Toleransi 0.5")
print("Hasil (x1, x2, x3) : {0}".format(x)) 
print("Nilai Error: {0}".format(error))