from numpy import array

#   Input sistem persamaan
A = array([[1, 1, 1, 6],
           [1, 2, -1, 2],
           [2, 1, 2, 10]])
print A

#   Eliminasi gauss
m=A[1,0]/A[0,0]
A[1,0]=A[1,0]-m*A[0,0]
A[1,1]=A[1,1]-m*A[0,1]
A[1,2]=A[1,2]-m*A[0,2]
A[1,3]=A[1,3]-m*A[0,3]

m=A[2,0]/A[0,0]
A[2,0]=A[2,0]-m*A[0,0]
A[2,1]=A[2,1]-m*A[0,1]
A[2,2]=A[2,2]-m*A[0,2]
A[2,3]=A[2,3]-m*A[0,3]

m=A[2,1]/A[1,1]
A[2,1]=A[2,1]-m*A[1,1]
A[2,2]=A[2,2]-m*A[1,2]
A[2,3]=A[2,3]-m*A[1,3]

print A

#   proses substitusi mundur

X[3,0]=A[3,4]/A[3,3]
X[2,0]=A[2,4]-A[2,3]*X[3,0]/A[2,2]
X[1,0]=A[1,4]-((A[1,2]*X[2,0])+(A[1,3]*X[3,0]))/A[1,1]

print X