import numpy as np

# define matrix

A=np.array ([[1,1,1], [1,2,-1], [2,1,2]], float)
B=np.array ([6,2,10], float)

n=len(A)

# eliminasi gauss

for k in range (0, n-1)
    for i in range (k+1, n):
        if A[i, k]!=0 :
            lam = A[i, k]/A[k, k]
            A[i, k:n] = A[i, k:n]-(A[k, k:n]*lam)
            B[i] = B[i]-(B[k]*lam)

print ('matrix A :', '\n', A)

# back substitution
x=np.zeros(n,float)
for m in range (n-1, -1, -1):
    x[m] = (B[m]-np.dot(A[m, m+1:n], x[m+1:n]))/A[m,m]
    print ('nilai X', m+1, '=', x[m])